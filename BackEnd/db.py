import psycopg2

def insertRow(date):
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
        INSERT INTO daily_activities (activity_date, gym, ticket, errand)
        VALUES (%s, %s, %s, %s)
    """

    date_value = date  
    gym_value = False           
    ticket_value = False       
    errand_value = False       

    cursor.execute(insert_query, (date_value, gym_value, ticket_value, errand_value))
    
    connection.commit()

    cursor.close()
    connection.close()

def updateRowFromDate(date, task, complete):
    connection = psycopg2.connect(
        dbname="tasks",
        user="postgres",
        password="password",
        host="127.0.0.1",
        port="5432"
    )
    print("Connected to the database!")
    cursor = connection.cursor()

    update_gym_query = """
        UPDATE daily_activities
        SET gym = %s
        WHERE activity_date = %s
    """

    update_ticket_query = """
        UPDATE daily_activities
        SET ticket = %s
        WHERE activity_date = %s
    """

    update_errand_query =  """
        UPDATE daily_activities
        SET errand = %s
        WHERE activity_date = %s
    """
    num_rows = -1
    if task == "fitnessButton":
        num_rows = cursor.execute(update_gym_query, (complete, date_value))
    elif task == "ticketButton":
        num_rows = cursor.execute(update_ticket_query, (complete, date_value))
    elif task == "errandButton":
        num_rows = cursor.execute(update_errand_query, (complete, date_value))

    connection.commit()

    if num_rows > 0:
        print("Row update successful")
    elif num_rows == 0:
        print("No row found for the given date")
        insertRow(date)
        updateRowFromDate(date, task, complete)
    else:
        print("No button selected")

    cursor.close()
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
        WHERE activity_date = %s
    """
    date_value = date

    cursor.execute(select_query, (date_value,))

    row = cursor.fetchone()

    if row:
        print(row)
    else:
        print('No row found for the given date')
        insertRow(date)
        row = getRowFromDate(date)

    cursor.close()
    connection.close()

    return row

    


