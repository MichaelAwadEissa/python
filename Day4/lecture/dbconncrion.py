import psycopg2
import sys

# Global variables for connection configuration
host = 'localhost'
user = 'iti'
password = '123'
dbname = 'python-fayoum'

# Function to connect to the database
def connect():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=dbname
        )
        return connection
    except Exception as e:
        print(f"Connection failed: {e}")
        sys.exit(1)

# Function to create a table
def create_table(query):
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print("Table created successfully.")
    except Exception as e:
        print(f"Exception occurred while creating table: {e}")
    finally:
        cur.close()
        conn.close()

# Function to select data from a table
def select_from_table(table_name):
    conn = connect()
    query = f'SELECT * FROM {table_name};'
    try:
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return data
    except Exception as e:
        print(f"Exception occurred while selecting data: {e}")
        return []
    finally:
        cur.close()
        conn.close()

# Function to insert a new trainee into the table
def insert_trainee(id, name, track):
    conn = connect()
    query = f"INSERT INTO TRAINEEDATA (ID, NAME, TRACKID) VALUES (%s, %s, %s);"
    try:
        cur = conn.cursor()
        cur.execute(query, (id, name, track))
        conn.commit()
        print("Trainee inserted successfully.")
    except Exception as e:
        print(f"Exception occurred while inserting trainee: {e}")
    finally:
        cur.close()
        conn.close()

# Function to update a trainee's information
def update_trainee(id, name, track):
    conn = connect()
    query = f"UPDATE TRAINEEDATA SET NAME = %s, TRACKID = %s WHERE ID = %s;"
    try:
        cur = conn.cursor()
        cur.execute(query, (name, track, id))
        conn.commit()
        print("Trainee updated successfully.")
    except Exception as e:
        print(f"Exception occurred while updating trainee: {e}")
    finally:
        cur.close()
        conn.close()

# Example usage
if __name__ == "__main__":
    # Create table example
    create_table_query = """
    CREATE TABLE IF NOT EXISTS TRAINEEDATA (
        ID SERIAL PRIMARY KEY,
        NAME VARCHAR(50),
        TRACKID INT
    );
    """
    create_table(create_table_query)

    # Insert a trainee example
    insert_trainee(1, 'John Doe', 101)

    # Select all trainees example
    trainees = select_from_table('TRAINEEDATA')
    print(trainees)

    # Update a trainee example
    update_trainee(1, 'John Smith', 102)

    # Select all trainees again to see updates
    trainees = select_from_table('TRAINEEDATA')
    print(trainees)
