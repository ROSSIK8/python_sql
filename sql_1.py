import psycopg2

from config import *
from funcs import *

if __name__ == '__main__':
    with psycopg2.connect(database=database, user=user, password=password) as conn:
        create_db(conn)


        add_client(conn, 'Sanzhay', 'Ayurov', 'ayurov2004@gmail.com')
        add_client(conn, 'Luffy', 'Monkey D.', 'ML@email.ru')
        add_client(conn, 'Zoro', 'Roarono', 'RZ@bk.ru')
        add_client(conn, 'Алишер', 'Моргенштерн', 'МА@email.ru')
        add_client(conn, 'Abc', 'Efg', 'abcefg@email.ru')
        add_client(conn, 'Абв', 'Где', 'abvgde@bk.ru')


        add_phone(conn, 1, '+7(999)-677-82-67')
        add_phone(conn, 1, '+7(914)-126-81-78')
        add_phone(conn, 3, '+7(999)-999-99-99')
        add_phone(conn, 5, '+7(555)-555-55-55')
        add_phone(conn, 4, '+7(666)-666-66-66')

        delete_phone(conn, '+7(555)-555-55-55')
        change_client(conn, 4, 'Victor', 'Tsoy', 'TV@gmail.com')

        delete_client(conn, 6)


        find_client(conn, last_name='Ayurov')
        print()
        find_client(conn, last_name='Monkey D.')
        print()
        find_client(conn, last_name='Roarono')
        print()
        find_client(conn, phone='+7(914)-126-81-78')
        print()
        find_client(conn, phone='+7(999)-999-99-99')