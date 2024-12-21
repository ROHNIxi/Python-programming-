""
"""
There are few libraries in python, where the name of library
given at installation time is different and while importing,
the library name is different. Sometimes new versions of
libraries comes with new names.
import speech_recognition

For installation library name is: SpeechRecognition

import speech_recognition 
"""

"""
Database:
Types of databases: multiple types but two are majorly used:
1. Relational Database
2. Non-relational Database

1. Relational Database: data is stored in the form of
tables and tables are connected through some keys. 
Primary Key: Unique and not null
Relational databases are called SQL databases.
SQL: Structured Query Langauge. A very popular langauge
used in relational databases.
Examples: MySQL, Oracle, MS-SQL Server, MS-Access, PostGre-SQL

Non-relational database: No-sql databases. Data is available
in multiple structures, and one of the most popular structure
or type of non-relational database is stored in the form
of key-value pairs.
Examples: MongoDB, Cassandra Server...


Relational databases: MySQL Database
For installation: CETPA Video
At the time of installation: 
Master Login: user id: root,
password to set at the time of installation:
user=root, password: root123
MySQL community edition

There are two options to works on database:
1. Directly install the database and start writing
the queries.
2. We can install LAMP, WAMP or XAMP Server on our
machine and then use database: Here you can work in
GUI kind of environment. 

Database Server: Collection of databases.
Database: Collection of Tables
Table: Collection of Columns (Fields)
or Collection of Rows (Records) and Columns.

99% SQL queries will be same for all relational database.
1% there will be some change in MySql, Oracle, 
MS-SQL Server and other databases. 

SQL queries are terminated by semicolon.

Types of SQL Queries:
1. DDL : Data Definition Language
2. DQL : Data Query Language
3. DML : Data Manipulation Langauge/Data Modification Langauge
4. DCL : Data Control Language
5. TCL : Transaction Control Langauge   

1. DDL : Data Definition Language: How to create things
at root level ie at basic level.
create table table_name(comma separated columns_names column_data_types)
create database database_name
drop database database_name
drop table table_name

2. DQL : Data Query Language: To retrieve the data
from database but won't make any changes in the data.
select (column_names) from table_name where_condition
select * from table_name

3. DML : Data Manipulation Langauge: We will make
some changes in the data.
insert into table_name (column_names) values(actual_values)
insert into table_name values(all_actual_values)

delete from table_name where_condition

update table_name set column_name=column_value where_condition

"""
# #New Program
# L1=[10,20,30]
# L1.clear()
# print(L1)

# #New Program
# L1=[10,20,30]
# del L1
# print(L1)

"""
Till now we have discussed how to work on different
sql queries in MySQL Server.
If you want to learn more: There is a separate 4 to
6 weeks course at CETPA and you can join it.
"""

"""
Database Connectivity: ie we run the query in
python and it should be executed in database

For Database Connectivity: We need to have
1. IP Address: If database is installed in our machine:
Local IP Address of each machine: 127.0.0.1
and this address is called 'localhost'
2. User Id: ie user name
user=root
3. Password: 
pwd=root123
4. Database name: db1 (Can be given through queries)
5. Port: 3306  (Optional)
"""



