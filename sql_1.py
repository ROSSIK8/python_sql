import psycopg2
from funcs import *


with psycopg2.connect(database='netolog_db', user='postgres', password='april082004') as conn:
    with conn.cursor() as cur:
        cur.execute(create_db())

        conn.commit()

        cur.execute(add_client('Sanzhay', 'Ayurov', 'ayurov2004@gmail.com', '+7(914)-126-81-78, +7(999)-677-82-67'))
        cur.execute(add_client('Luffy', 'Monkey D.', 'ML@email.ru'))
        cur.execute(add_client('Zoro', 'Roarono', 'RZ@bk.ru'))
        cur.execute(add_client('Алишер', 'Моргенштерн', 'МА@email.ru'))
        cur.execute(add_client('Abc', 'Efg', 'abcefg@email.ru', '+7(999)-888-88-88'))
        cur.execute(add_client('Абв', 'Где', 'abvgde@bk.ru'))


        cur.execute(add_phone(3, '+7(999)-999-99-99'))

        cur.execute(change_client(4, 'Victor', 'Tsoy', 'TV@gmail.com'))

        cur.execute(delete_phone(5))

        cur.execute(delete_client(6))


        cur.execute(find_client(phone='+7(914)-126-81-78'))
        print(cur.fetchone())

        cur.execute(find_client(first_name='Luffy'))
        print(cur.fetchone())

        cur.execute(find_client(last_name='Roarono'))
        print(cur.fetchone())

        cur.execute(find_client(email='TV@gmail.com'))
        print(cur.fetchone())

        cur.execute(find_client(email='abcefg@email.ru'))
        print(cur.fetchone())