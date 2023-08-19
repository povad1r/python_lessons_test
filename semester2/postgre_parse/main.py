import psycopg2








def add_data(email:str, new_age: int):

    connection = psycopg2.connect(
        host='ep-old-heart-356850.eu-central-1.aws.neon.tech',
        port='5432',
        database='neondb',
        user='povad1r',
        password='mUlN0H2hIspZ'
        )

    cursor = connection.cursor()

    query = "UPDATE students SET age = %s WHERE email = %s"
    cursor.execute(query, (new_age, email)) 
    connection.commit()
    cursor.close()
    connection.close()