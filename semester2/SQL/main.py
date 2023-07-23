import psycopg2
from getpass import getpass
import os
from dotenv import load_dotenv

load_dotenv()


def registration():
    username = input('Username: ')
    password = getpass()
    email = input('Email: ')

    try:
        connection = psycopg2.connect(
            host='ep-old-heart-356850.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='povad1r',
            password='mUlN0H2hIspZ'
        )

        cursor = connection.cursor()
        query = 'SELECT email FROM users WHERE email = %s'
        cursor.execute(query, (email,))
        if cursor.fetchone():
            print('User has already been registered')
        else:
            query = 'INSERT INTO users (username, password, email) VALUES (%s, %s, %s)'
            cursor.execute(query, (username, password, email)) 
            connection.commit()
            print('User successfully registered!')
    except Exception as error:
        print('An error occurred while registering user:', error)
    finally:
        cursor.close()
        connection.close()



def login():
    password = getpass()
    email = input('Email: ')

    try:
        connection = psycopg2.connect(
            host='ep-old-heart-356850.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='povad1r',
            password='mUlN0H2hIspZ'
        )

        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (email,password))

        user = cursor.fetchone()
        print(user) 

        if user:
            print('You have logged in!')
        else:
            print('Invalid login credentials')
    except Exception as error:
        print('An error occurred while logging: ', error)




if __name__ == '__main__':
    match input('Select an action: (login/register): '):
        case 'login':
            login()
        case 'register':
            registration()
        case _:
            print('Invalid action')
