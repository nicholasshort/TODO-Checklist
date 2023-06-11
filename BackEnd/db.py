import psycopg2

def updateTable():
    connection = psycopg2.connect(
        dbname='tasks',
        user='postgres',
        password='password',
        host='127.0.0.1',
        port='5432'
    )
    print("Connected to the database!")

    # Perform operations on the database here
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM daily_activities")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    connection.close()

updateTable()