def create_db(conn):
    with conn.cursor() as cur:
        cur.execute('''CREATE TABLE IF NOT EXISTS customer_information(
                       id SERIAL PRIMARY KEY,
                       first_name VARCHAR(40) NOT NULL,
                       last_name VARCHAR(40) NOT NULL,
                       email VARCHAR(40) UNIQUE NOT NULL);
                       
                       CREATE TABLE IF NOT EXISTS client_phones(
                       id SERIAL PRIMARY KEY,
                       client_id integer REFERENCES customer_information(id),
                       phones VARCHAR(40) UNIQUE);''')
        conn.commit()


def add_client(conn, first_name, last_name, email):
    with conn.cursor() as cur:
        cur.execute('''INSERT INTO customer_information(first_name, last_name, email)
                       VALUES(%s, %s, %s)''', (first_name, last_name, email))
        conn.commit()
    # else:
    #     info_client = f'''INSERT INTO customer_information(first_name, last_name, email, phones)
    #                               VALUES('{first_name}', '{last_name}', '{email}', '{phones}')'''
    #     return info_client

def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute('''INSERT INTO client_phones(client_id, phones)
                       VALUES(%s, %s)''', (client_id, phone))
        conn.commit()

def change_client(conn, client_id, first_name=None, last_name=None, email=None):
    with conn.cursor() as cur:
        cur.execute('''DELETE FROM client_phones
                       WHERE client_id = %s;
        
                       UPDATE customer_information
                       SET first_name = %s,
                           last_name = %s,
                           email = %s
                       WHERE id = %s''', (client_id, first_name, last_name, email, client_id))
        conn.commit()

def delete_phone(conn, phone):
    with conn.cursor() as cur:
        cur.execute('''DELETE FROM client_phones
                        WHERE phones LIKE %s ''', (phone,))
        conn.commit()

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute('''DELETE FROM customer_information
                         WHERE id = %s''', (client_id,))
        conn.commit()

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    dict_info = {'first_name': first_name,
                 'last_name': last_name,
                 'email': email,
                 'phone': phone}
    some_info = []
    for key, val in dict_info.items():
        if val != None:
            some_info += [key, val]
            break

    if some_info[0] != 'phone':
        with conn.cursor() as cur:
            cur.execute('''SELECT ci.id, first_name, last_name, email, phones FROM customer_information ci
                           LEFT JOIN client_phones cp ON ci.id = cp.client_id 
                           WHERE ''' + some_info[0] + ' = ' + "'" + some_info[1] + "'")
            list_info = cur.fetchall()
            if len(list_info) > 1:
                new_list_info = list(list_info[0])
                for item in list_info[1:]:
                    new_list_info.append(item[-1])
                return print(new_list_info)
            return print(list(list_info[0]))

    with conn.cursor() as cur:
        cur.execute('''SELECT ci.id, first_name, last_name, email, phones FROM client_phones cp 
                       LEFT JOIN customer_information ci ON ci.id = cp.client_id 
                       WHERE ci.id = (SELECT ci.id FROM customer_information ci
                                      LEFT JOIN client_phones cp ON ci.id = cp.client_id 
                                      WHERE phones = %s)''', (phone,))
        list_info = cur.fetchall()
        if len(list_info) > 1:
            new_list_info = list(list_info[0])
            for item in list_info[1:]:
                new_list_info.append(item[-1])
            return print(new_list_info)
        return print(list(list_info[0]))


