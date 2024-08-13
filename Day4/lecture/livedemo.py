
# from Human import Human
# #create objct from human class
# obj1=Human(1,'aya ali','fayoum') #calling __init (self)
# obj2=Human(2,'mark ','fayoum')
# # obj3=Human()
# obj1.count=100#remove adddress of count set by value
# print(Human.count)#2
# print(obj1.count)#100
# print(obj2.count)#2
# print(Human.getcount())
# Human.measuretemp(37)
# Human.measuretemp(38)
# obj1.id=10
# obj1.name='aya ali'
# obj1.add='fayoum'
# # print(obj1.id,obj1.name,obj1.add)
# obj1.drink()
# #instance var
# obj1.age=10

# obj1.eat()

# obj2.drink()
# print(type(obj1),obj1)
# print(type(obj2),obj2)

import psycopg2
#prepare db connection info
host='localhost'
user='iti'
password='789456'
dbname='python-fayoum'
connection=psycopg2.connect( database=dbname,
            user=user,
            password=password,
            host=host
            )
# print(type(connection),connection)
cur=connection.cursor()
cur.execute("select * from traineedata;")
# cur.commit()   #must be in case of insert
# traineeid=cur.fetchone()
# #insert,update,delete
# connection.commit()
recoreds=cur.fetchall()
# recoreds object of [(1,'aya',1),(),()]
print(recoreds)
for recored in recoreds:
    print('ID:',recored[0],"Name:",recored[1],"Track:",recored[2],sep='\n',end='\n============')




##MY PRACTICE 
# import psycopg2
# import sys

# # Global variables for connection configuration
# host = 'localhost'
# user = 'iti'
# password = '789456'
# dbname = 'python-fayoum'

# Connect to the database
# def connect():
#     try:
#         connection = psycopg2.connect(
#             host=host,
#             user=user,
#             password=password,
#             dbname=dbname
#         )
#         return connection
#     except Exception as e:
#         print(f"Connection failed: {e}")
#         sys.exit(1)  # Exit the program if connection fails

# # Create a table with the given query
# def create_table(query):
#     conn = connect()
#     try:
#         cur = conn.cursor()
#         cur.execute(query)
#         conn.commit()
#         print("Table created successfully.")
#     except Exception as e:
#         print(f"Exception occurred while creating table: {e}")
#     finally:
#         cur.close()
#         conn.close()

# # Select data from the specified table
# def select_from_table(table_name):
#     conn = connect()
#     query = f'SELECT * FROM {table_name};'
#     try:
#         cur = conn.cursor()
#         cur.execute(query)
#         data = cur.fetchall()
#         return data
#     except Exception as e:
#         print(f"Exception occurred while selecting data: {e}")
#         return []
#     finally:
#         cur.close()
#         conn.close()

