import psycopg2
import sys

# Global variables for connection configuration
host = 'localhost'
user = 'iti'
password = '789456'
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

# Function to insert data into a table
def insert(table_name, columns, values):
    conn = connect()
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
    try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print(f"Data inserted into {table_name} successfully.")
    except Exception as e:
        print(f"Exception occurred while inserting data: {e}")
    finally:
        cur.close()
        conn.close()

# Function to update data in a table
def update(table_name, set_clause, condition):
    conn = connect()
    query = f"UPDATE {table_name} SET {set_clause} WHERE {condition};"
    try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print(f"Data in {table_name} updated successfully.")
    except Exception as e:
        print(f"Exception occurred while updating data: {e}")
    finally:
        cur.close()
        conn.close()

# Function to select data from a table
def select(table_name, columns='*', condition=None):
    conn = connect()
    query = f"SELECT {columns} FROM {table_name}"
    if condition:
        query += f" WHERE {condition}"
    query += ";"
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

# Function to delete data from a table
def delete(table_name, condition):
    conn = connect()
    query = f"DELETE FROM {table_name} WHERE {condition};"
    try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print(f"Data deleted from {table_name} successfully.")
    except Exception as e:
        print(f"Exception occurred while deleting data: {e}")
    finally:
        cur.close()
        conn.close()

# Example usage
if __name__ == "__main__":
    # Create the 'trainee' table
    create_table("""
    CREATE TABLE IF NOT EXISTS trainee (
        ID SERIAL PRIMARY KEY,
        NAME VARCHAR(50),
        TRACKID INT
    );
    """)

    # Create the 'track' table
    create_table("""
    CREATE TABLE IF NOT EXISTS track (
        TRACKID SERIAL PRIMARY KEY,
        TRACKNAME VARCHAR(50)
    );
    """)

    # Insert a record into the 'trainee' table
    insert('trainee', 'NAME, TRACKID', "'John Doe', 1")

    # Insert a record into the 'track' table
    insert('track', 'TRACKNAME', "'Python'")

    # Update a record in the 'trainee' table
    update('trainee', "NAME = 'Jane Doe'", "ID = 1")

    # Select and print all records from the 'trainee' table
    trainees = select('trainee')
    print(trainees)

    # Delete a record from the 'trainee' table
    delete('trainee', "ID = 1")
