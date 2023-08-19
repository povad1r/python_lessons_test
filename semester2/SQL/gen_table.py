import psycopg2

def registration():
        connection = psycopg2.connect(
            host='ep-old-heart-356850.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='povad1r',
            password='mUlN0H2hIspZ'
        )

        cursor = connection.cursor()

        query = 'INSERT INTO students (name, age, email) VALUES (%s, %s, %s)'
        cursor.execute(query, ('Kolya', '16', 'nick@gmail.com'))
        connection.commit()


        connection.close()
        cursor.close()


registration()
