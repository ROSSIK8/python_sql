def create_db():
    table = '''CREATE TABLE IF NOT EXISTS customer_information(
                           id SERIAL PRIMARY KEY,
                           first_name VARCHAR(40) NOT NULL,
                           last_name VARCHAR(40) NOT NULL,
                           email VARCHAR(40) UNIQUE NOT NULL,
                           phones VARCHAR(40) UNIQUE);'''
    return table

def add_client(first_name, last_name, email, phones=None):
    if phones == None:
        info_client = f'''INSERT INTO customer_information(first_name, last_name, email, phones)
                          VALUES('{first_name}', '{last_name}', '{email}', NULL)'''
        return info_client
    else:
        info_client = f'''INSERT INTO customer_information(first_name, last_name, email, phones)
                                  VALUES('{first_name}', '{last_name}', '{email}', '{phones}')'''
        return info_client

def add_phone(client_id, phone_or_phones):
    update_phone = f'''UPDATE customer_information
                       SET phones = '{phone_or_phones}' 
                       WHERE id = {client_id}'''
    return update_phone

def change_client(client_id, first_name=None, last_name=None, email=None, phones=None):
    if phones == None:
        update_client = f'''UPDATE customer_information
                            SET first_name = '{first_name}',
                                last_name = '{last_name}',
                                email = '{email}',
                                phones = NULL
                            WHERE id = {client_id}'''
        return update_client
    else:
        update_client = f'''UPDATE customer_information
                                    SET first_name = '{first_name}',
                                        last_name = '{last_name}',
                                        email = '{email}',
                                        phones = '{phones}'
                                    WHERE id = {client_id}'''
        return update_client

def delete_phone(client_id):
    delete_phone_ = f'''UPDATE customer_information
                        SET phones = NULL
                        WHERE id = {client_id}
                        '''
    return delete_phone_

def delete_client(client_id):
    delete_client_ = f'''DELETE FROM customer_information
                         WHERE id = {client_id}'''

    return delete_client_

def find_client(first_name=None, last_name=None, email=None, phone=None):
    dict_info = {'first_name': first_name,
                 'last_name': last_name,
                 'email': email,
                 'phones': phone}
    some_info = []
    for key, val in dict_info.items():
        if val != None:
            some_info += [key, val]
            break
    client = f'''SELECT * FROM customer_information
                       WHERE {some_info[0]} LIKE '%{some_info[1]}%' '''
    return client

