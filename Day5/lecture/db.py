import psycopg2

# Step 3.1: Connect to the PostgreSQL database
def connect():
    try:
        connection = psycopg2.connect(
            database="fayoumdemo",
            user="iti",
            password="123",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as error:
        print(f"Error connecting to PostgreSQL database: {error}")
        return None

# Step 3.2: Create a new record
def createtrack(trackobj):
    connection = connect()
    cursor = connection.cursor()
    tablename='track'
    values=(trackobj.id,trackobj.name)
    try:
        scol = ''
        for val in values:
            scol += '%s'
        insert_query = f"""INSERT INTO {tablename}  VALUES ({scol}) RETURNING id;"""
        cursor.execute(insert_query, values)
        employee_id = cursor.fetchone()[0]
        connection.commit()
        print(f"{tablename} created with ID: {employee_id}")
    except Exception as error:
        print(f"Error creating employee: {error}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


def create(tablename,*values):
    connection = connect()
    cursor = connection.cursor()
    
    try:
        scol=''
        for val in values:
            scol+='%s'
        insert_query = f"""INSERT INTO {tablename}  VALUES ({scol}) RETURNING id;"""
        cursor.execute(insert_query, values)
        employee_id = cursor.fetchone()[0]
        connection.commit()
        print(f"{tablename} created with ID: {employee_id}")
    except Exception as error:
        print(f"Error creating employee: {error}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# Step 3.3: Read records
def read_employees():
    connection = connect()
    cursor = connection.cursor()
    
    try:
        select_query = "SELECT * FROM employees;"
        cursor.execute(select_query)
        employees = cursor.fetchall()
        for employee in employees:
            print(employee)
    except Exception as error:
        print(f"Error reading employees: {error}")
    finally:
        cursor.close()
        connection.close()

# Step 3.4: Update a record
def update_employee(employee_id, name, age, department):
    connection = connect()
    cursor = connection.cursor()    
    try:
        update_query = """UPDATE employees SET name = %s, age = %s, department = %s WHERE id = %s;"""
        cursor.execute(update_query, (name, age, department, employee_id))
        connection.commit()
        print(f"Employee with ID {employee_id} updated.")
    except Exception as error:
        print(f"Error updating employee: {error}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# Step 3.5: Delete a record
def delete_employee(employee_id):
    connection = connect()
    cursor = connection.cursor()
    
    try:
        delete_query = "DELETE FROM employees WHERE id = %s;"
        cursor.execute(delete_query, (employee_id,))
        connection.commit()
        print(f"Employee with ID {employee_id} deleted.")
    except Exception as error:
        print(f"Error deleting employee: {error}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# Step 3.6: Main function to demonstrate CRUD operations
if __name__ == "__main__":
    # Create a new employee
    create_employee('John Doe', 30, 'Engineering')
    
    # Read all employees
    print("\nEmployees:")
    read_employees()
    
    # Update an employee
    update_employee(1, 'Jane Doe', 32, 'Marketing')
    
    # Read all employees again to see the update
    print("\nEmployees after update:")
    read_employees()
    
    # Delete an employee
    delete_employee(1)
    
    # Read all employees again to see the deletion
    print("\nEmployees after deletion:")
    read_employees()
