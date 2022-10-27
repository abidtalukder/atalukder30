# Abid Talukder, Raven Tang, Craig Chen
# SoftDev
# K18: (Python+SQLite)3: A Mare Widge Made in Hebben
# 2022-10-26
# time spent: 0.8 Hours

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

delete_table ="DROP TABLE IF EXISTS students" # students table, delete if already exists
c.execute(delete_table)
create_table = "create table students(name text, age int, id int);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(create_table)    # run SQL statement

# Opening CSV file for iteration
with open('students.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader: 
        c.execute(f'insert into students values(\'{row["name"]}\',{row["age"]},{row["id"]});')

delete_table ="DROP TABLE IF EXISTS courses"
c.execute(delete_table)
create_table = "create table courses(code text, mark int, id int);"          
c.execute(create_table)    # run SQL statement

# Opening CSV file for iteration
with open('courses.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader: 
        c.execute(f'insert into courses values(\'{row["code"]}\',{row["mark"]},{row["id"]});')

#==========================================================

db.commit() #save changes
c.execute("select * from students;")
students = (c.fetchall())

print("name | age | id")
print()
for group in students:
    print(f'{group[0]} | {group[1]} | {group[2]}')

print()
print("**********")
print()

c.execute("select * from courses;")
courses = (c.fetchall())

print("code | mark | id")
print()
for group in courses:
    print(f'{group[0]} | {group[1]} | {group[2]}')

db.close()  #close database


