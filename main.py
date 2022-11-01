# import inspect
# import os
#
# ############### Date time ############
# from datetime import datetime
# todaysDate = datetime.now()
# print(todaysDate.day)
#
# ##### Formate #########
#
# year = todaysDate.strftime("%Y")
#
# print(year)
#
#
# year = todaysDate.strftime("%y")
#
# print(year)
#
# month = todaysDate.strftime("%M")
#
# print(month)
#
# month = todaysDate.strftime("%m")
#
# print(month)
#
#
# day = todaysDate.strftime("%D")
#
# print(day)
#
# day = todaysDate.strftime("%d")
#
# print(day)
#
# time = todaysDate.strftime('%H:%M:%S')
# print(time)
#
# timeAnddate = todaysDate.strftime('%H:%M:%S, %d:%m:%Y')
# print(timeAnddate)
#
#
# timeAnddate = todaysDate.strftime('%H/%M/%S, %d/%m/%Y')
# print(timeAnddate)
#
# ###############################
#
# ###### OS Module #############
#
# print(os.getcwd())
#
# print(os.listdir())
#
# os.mkdir('test')
#
# print(os.listdir())
#
# os.rmdir('test')
#
# print(os.listdir())
#
# os.mkdir('TestDir')
#
# print(os.listdir())
#
# ###########################
#
# ####### Inspect ###########
#
# class Greeter:
#     def __init__(self, name):
#         self.name = name
#
#     def sayHello(self):
#         print(f"Hello {self.name}")
#
#     def sayGoodbye(self):
#         print(f"Bye {self.name}")
#
# greet = Greeter("Ali")
# greet.sayHello()
# greet.sayGoodbye()
#
# stringVar = 'This is available'
#
# numericVar = 42.42
#
# print(f'class ID = {id(greet)}')
#
# print(f'class type = {type(greet)}')
#
# print(f'class directory = {dir(greet)}')
#
# print(f'stringVar ID = {id(stringVar)}')
#
# print(f'stringVar type = {type(stringVar)}')
#
# print(f'stringVar Dir = {dir(stringVar)}')
#
#
# inspect.getmembers(stringVar)
#

"""
create connection
close connection
create table

"""
#
# import sqlite3
# from sqlite3 import Error
#
#
# def create_connection(db_file_name):
#     try:
#         conn = sqlite3.connect(db_file_name)
#         print('The sqlite is connected')
#         return conn
#     except Error as e:
#         print(e)
#
#
# def close_connection(conn):
#     if conn:
#         conn.close()
#         print('Connection is closed.')
#
#
# def create_table_in_db(conn, create_table_sql):
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#         print('Success, table created.')
#
#     except Error as e:
#         print(e)
#
#
# def create_table():
#     database = r'/home/sadam/python/python-beta-level-2/database.db'
#     sql_create_projects_table = ''' CREATE TABLE IF NOT EXISTS STUDENTS(
#     id integer PRIMARY KEY,
#     name text NOT NULL,
#     gpa integer,
#     admin_date text
#     );
#     '''
#     conn = create_connection(database)
#     if conn is not None:
#         create_table_in_db(conn, sql_create_projects_table)
#     else:
#         print('Error, can"t create database connection.')
#
#     close_connection(conn)
#
#
# create_table()
#
#
# def add_student(conn, student):
#     sql = '''INSERT INTO STUDENTS(name, gpa, admin_date)
#     VALUES(?,?,?)
#     '''
#
#     cur = conn.cursor()
#     cur.execute(sql, student)
#     return cur.lastrowid
#
#
# def insert_values():
#     database = r'/home/sadam/python/python-beta-level-2/database.db'
#     conn = create_connection(database)
#     with conn:
#         student = ['Asad', 4.0, '2022']
#         std_id = add_student(conn, student)
#     add_student(conn, student)
#
#     print(f'Student ID is {std_id}'))
#     close_connection(conn)
#
#
# # insert_values()
#
#
# def read_student():
#     database = r'/home/sadam/python/python-beta-level-2/database.db'
#     conn = create_connection(database)
#     sql_string = 'SELECT * FROM STUDENTS'
#     cur = conn.cursor()
#     cur.execute(sql_string)
#     record = cur.fetchall()
#     print(record, '\n')
#     cur.close()
#     close_connection(conn)
#
#
# read_student()
