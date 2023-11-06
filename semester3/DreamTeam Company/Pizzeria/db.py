import sqlite3


try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    sqlite_create_table_query = '''CREATE TABLE order (
                                    id INTEGER PRIMARY KEY,
                                    order TEXT NOT NULL,
                                    email TEXT NOT NULL UNIQUE,
                                    joining_date datetime,
                                    salary REAL NOT NULL);'''

    cursor = sqlite_connection.cursor()
    print('База даних створена і підключена')
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print('Таблиця створена')
    cursor.close()

except sqlite3.Error as error:
    print('Помилка підключення до', error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print('Connection закрито')
