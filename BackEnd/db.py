import psycopg2

def updateTable(task, complete):
    connection = psycopg2.connect(
        dbname='tasks',
        user='postgres',
        password='password',
        host='127.0.0.1',
        port='5432'
    )
    print("Connected to the database!")

    cursor = connection.cursor()

    insert_query = """
        INSERT INTO daily_activities (date, gym, ticket, errand)
        VALUES (%s, %s, %s, %s)
    """

    date_value = '2023-06-12'  
    gym_value = True           
    ticket_value = False       
    errand_value = True        

    cursor.execute(insert_query, (date_value, gym_value, ticket_value, errand_value))
    # # Perform operations on the database here
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM daily_activities")
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    connection.close()

def getRowFromDate(date):
    connection = psycopg2.connect(
        dbname="tasks",
        user="postgres",
        password="password",
        host="127.0.0.1",
        port="5432"
    )
    print("Connected to the database!")
    cursor = connection.cursor()

    select_query = """
        SELECT *
        FROM daily_activities
        WHERE date = %s
    """
    date_value = '2023-06-11'

    cursor.execute(select_query, (date_value,))

    row = cursor.fetchone()

    if row:
        print(row)
    else:
        print('No row found for the given date')

    cursor.close()
    connection.close()

    


