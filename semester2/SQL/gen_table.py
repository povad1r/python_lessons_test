import psycopg2



connection = psycopg2.connect(
    host='ep-old-heart-356850.eu-central-1.aws.neon.tech',
    port='5432',
    database='neondb',
    user='povad1r',
    password='mUlN0H2hIspZ'
    )

cursor = connection.cursor()

query = "SELECT * FROM students WHERE email LIKE '%k%'"
cursor.execute(query)
result = cursor.fetchall()
file = open('semester2\SQL\data.csv', 'w', encoding='utf-8')
file.write('Id, Name, Age, Email')
count = 0
for student in result: 
    file.write(f'\n{result[count]}')
    count += 1
file.close
print(result)

connection.commit()
cursor.close()
connection.close()
