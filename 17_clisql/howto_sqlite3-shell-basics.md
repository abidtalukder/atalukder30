# how-to :: SQLite3 Shell Basics
---
## Overview
SQLite is important because it allows us to use and manage databases, specifically relational databases. It's streamlined and fast, so it's a very useful platform.

### Estimated Time Cost: 0.5 hrs

### Prerequisites:

- Be familiar with general Terminal/Shell commands
- Bookmark documentation for [SQLite](https://www.sqlite.org/cli.html)
- Draft on paper the tables and information that you want to include and manage in your database

1. In Terminal, in the desired directory, create a database
    ```$ sqlite3 <database_name>```
	Ex:
    ```$ sqlite3 students```
2. Create a table within your database, inputting information about the datatype and name of each column. Available data types are TEXT (like a string), INTEGER, REAL, NUMERIC (default integer, but can hold floating point), and BLOB (no suggested/converted type). Don't forget the semicolon at the end of the line.
    ```sqlite> create table <table_name>(<first_col_name> <first_col_data_type>, <second_col_name> <second_col<data_type>, <...>);```
	Ex:
	```sqlite> create table student_info(osis integer, gpa numeric, address text);```
3. To populate a row of the table, insert values in the corresponding order of the columns. Again, don't forget the semicolon at the end of the line.
	```sqlite> insert into <table_name> values(<first_value>, <second_value>, <third_value>);```
	Ex:
	```
	sqlite> insert into student_info values(123, 100, "345 Chambers St");
	sqlite> insert into student_info values(456, 0, "123 Chambers St");
	sqlite> insert into student_info values(789, 50, "321 Chambers St");
	```
4. To show the entire table, use the * operator.
    ```sqlite> select * from <table_name>;```
	Ex:
	```sqlite> select * from student_info;```
	...should print out...
	```
	123|100|345 Chambers St
	456|0|123 Chambers St
	789|50|321 Chambers St
	```
5. To show just one column, use that column's name.
	```sqlite> select <col_name> from <table_name>```
	Ex:
	```sqlite> select address from student_info;```
	...should print out...
	```
	345 Chambers St
	123 Chambers St
	321 Chambers St
	```
6. Exit sqlite by Ctrl + D
### Resources
* (SQLite Documentation)[https://www.sqlite.org/cli.html]
* students sample database in this directory

---

Accurate as of (last update): 2022-10-24

#### Contributors:  
Clyde "Thluffy" Sinclair  
Craig Chen, pd2  
Raven (Ruiwen) Tang, pd2  
Abid Talukder, pd2  
