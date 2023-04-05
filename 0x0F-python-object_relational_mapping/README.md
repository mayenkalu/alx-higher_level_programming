# Python - Object Relational Mapping :page_with_curl: 
This project explores the concept of [Object Relational Mapping](https://www.fullstackpython.com/object-relational-mappers-orms.html). 
ORM is a special tool that connects two things - an object-oriented programming language and a relational database. It provides a way to store and retrieve data from a database using the programming language's objects, rather than writing complex SQL queries. This makes it easier for developers to work with databases and allows them to focus on the application logic instead of database management.
ORM helps take the information in the database and turn it into objects that can be used in the programming language. This makes it easier for developers to work with the information and focus on building the program, rather than worrying about managing the database. 

## Objectives :Bulb:

**Python programming is amazing** because its one of the most popular languages used by developers worldwide. It's known for its simplicity, readability, and versatility, making it an excellent choice for developing various applications. Python's syntax is concise and easy to learn, making it an ideal language for beginners. It also has a vast and active community, which means there are plenty of resources and support available. Python is widely used in various fields, including web development, data science, machine learning, artificial intelligence, and more. With its many advantages, Python programming truly is awesome.

**To connect to a MySQL database from a Python script**, you'll need to use a library called "mysql-connector-python." You can install it using pip, like this:
```
pip install mysql-connector-python
```
Once you have the library installed, you can use the following code to connect to your MySQL database:
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

print(mydb)
```
In this code, you need to replace the placeholders with your actual credentials for the host, username, password, and database.

Once you've established a connection to your MySQL database, you can use the following code *to select rows from a table*:
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM yourtable")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```
In this code, you need to replace the placeholders with your actual credentials for the host, username, password, database, and table. The SELECT statement retrieves all the rows from the table, and the fetchall() method returns all the rows as a list of tuples. You can then iterate over the list and print each row.

**To insert rows into a MySQL table from a Python script**, you can use the following code:
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO yourtable (column1, column2, column3) VALUES (%s, %s, %s)"
val = ("value1", "value2", "value3")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```

**To map a Python class to a MySQL table**, you can use an ORM library like SQLAlchemy. Here's an example of how to do it:
```
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the connection to the MySQL database
engine = create_engine('mysql+mysqlconnector://username:password@localhost:3306/yourdatabase')

# Create the declarative base object
Base = declarative_base()

# Define the class that represents the table
class MyTable(Base):
    __tablename__ = 'mytable'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Add a new record to the table
new_record = MyTable(name='John', age=30)
session.add(new_record)
session.commit()

# Retrieve all records from the table
records = session.query(MyTable).all()
for record in records:
    print(record.id, record.name, record.age)
```
In this code, you define a class `MyTable` that inherits from `Base1`, which is the declarative base object. The `__tablename__` attribute specifies the name of the table in the database. Each attribute of the class corresponds to a column in the table. Once you define the class, you can use the `create_all` method of the metadata object to create the table if it doesn't exist.

To interact with the database, you create a session using the `sessionmaker` object and add records to the table using the `add` method of the session object. You can retrieve records from the table using the `query` method of the session object and iterate over the results. SQLAlchemy takes care of translating your Python code into SQL queries and mapping the results back to Python objects.

## Task Description
1. [0-select_states.py](./0-select_states.py)
    - Python script that uses MySQLdb to list all states in the database `hbtn_0e_0_usa`.
    - Usage: `./0-select_states.py <mysql username> <mysql password>  <database name>`. 
    - Results are ordered by ascending `states.id`.
2. [1-filter_states.py](./1-filter_states.py)
    - Python script that uses MySQLdb to list all states with names starting with `N` in the database `hbtn_0e_0_usa`. 
    - Usage: `./1-filter_states.py <mysql username> <mysql password>  <database name>`. 
    - Results are ordered by ascending `states.id`.
3. [2-my_filter_states.py](./2-my_filter_states.py) 
    - Python script that uses MySQLdb to display all values matching a given name in the `states` table of the database `hbtn_0e_0_usa`.
    - Usage: `./2-my_filter_states.py <mysql username> <mysql password>  <database name> <state name searched>`.
    - Results are ordered by ascending `states.id`. Uses string formatting to construct the SQL query.
4. [3-my_safe_filter_states.py](./3-my_safe_filter_states.py) 
    - Python script that uses MySQLdb to display all values matching a given name in the `states` table of the database `hbtn_0e_0_usa`.
    - Usage: `./3-my_safe_filter_states.py <mysql username> <mysql password>  <database name> <state name searched>`. 
    - Results are ordered by ascending `states.id`. Safe from SQL injections.
5.  [4-cities_by_state.py](./4-cities_by_state.py) 
    - Python script that uses MySQLdb to list all cities from the database `hbtn_0e_4_usa`.
    - Usage: `./4-cities_by_state.py <mysql username> <mysql password>   <database name>`.
    - Results are ordered by ascending `cities.id`.
6.  [5-filter_cities.py](./5-filter_cities.py)
    - Python script that uses MySQLdb to list all cities of a given state in the database `hbtn_0e_4_usa`.
    - Usage: `./5-filter_cities.py <mysql username> <mysql password> <database name>`.
    - Results are sorted by ascending `cities.id`.
6.  [model_state.py](./model_state.py) 
    - Python module defining a class `State` that inherits from SQLAlchemy `Base` and links to the MySQL table `states`.
7.  [7-model_state_fetch_all.py](./7-model_state_fetch_all.py)
    - Python script that uses SQLAlchemy to list all `State` objects from the database `hbtn_0e_6_usa`.
    - Usage: `./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>`.
    - Results are sorted by ascending `states.id`.
8.  [8-model_state_fetch_first.py](./8-model_state_fetch_first.py)
    - Python script that uses SQLAlchemy to print the first `State` object from the database `hbtn_0e_6_usa`, ordered by `states.id`.
    - Usage: `./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>`.
    - If the `states` table is empty, prints `Nothing`.
9.  [9-model_state_filter_a.py](./9-model_state_filter_a.py)
    - Python script that uses SQLAlchemy to list all `State` objects that contain the letter `a` in the database `hbtn_0e_6_usa`.
    - Usage: `./9-model_state_filter_a.py <mysql username> <mysql password> <database name>`.
    - Results are ordered by ascending `states.id`.
10. [10-model_state_my_get.py](./10-model_state_my_get.py)
    - Python script that uses SQLAlchemy to print the `id` of the `State` object with name matching that passed as argument in the database `hbtn_0e_6_usa`.
    - Usage: `./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state searched name>`.
    - Displays the `id` of the matched `State`.
    - If no match is found, prints `Not found`.
11. [11-model_state_insert.py](./11-model_state_insert.py)
    - Python script that uses SQLAlchemy to add the `State` object "Louisiana" to the database `hbtn_0e_6_usa`.
    - Usage: `./11-model_state_insert.py <mysql username> <mysql password> <database name>`.
    - Prints the `id` of the new `State` after creation.
12. [12-model_state_update_id_2.py](./12-model_state_update_id_2.py)
    - Python script that uses SQLAlchemy to change the name of the `State` object with `id = 2` in the database `hbtn_0e_6_usa` to "New Mexico".
    - Usage: `./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>`.
13. [13-model_state_delete_a.py](./13-model_state_delete_a.py)
    - Python script that uses SQLAlchemy to delete all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.
    - Usage: `./13-model_state_delete_a.py <mysql username> <mysql password> <database name>`. 
14. [model_city.py](./model_city.py)
    - Python module defining a class `City` that inherits from SQLAlchemy `Base` and links to the MySQL table `cities`.
    - Includes class attribute `state_id` that is a foreign key to `states.id`.
15. [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py)
    - Python script that uses SQLAlchemy to list all `City` objects in the database `hbtn_0e_14_usa`.
    - Usage: `./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>`.
    - Results are sorted by ascending `cities.id`.
16. [relationship_state.py](./relationship_state.py)
    - Python module defining a class `State` that inherits from SQLAlchemy `Base` and links to the MySQL table
  `states`.
    - Identical to the `State` class defined in [model_state.py](./model_state.py). 
    - Includes class attribute `classes` that represents a relationship with the class `City`.
    - If the `State` object is deleted, all linked `City` objects are also deleted. `State` objects are backreferenced to `City` objects as `state`.
17. [relationship_city.py](./relationship_city.py)
    - Python module defining a class `City` that inherits from SQLAlchemy `Base` and links to the MySQL table
  `cities`.
    - Identical to the `City` class defined in [model_city.py](./model_city.py).
18. [100-relationship_states_cities.py](./100-relationship_states_cities.py)
    - Python script that uses SQLAlchemy to add the `State` "California" with `City` "San Francisco" to the database `hbtn_0e_100_usa`.
    - Usage: `./100-relationship_states_cities.py <mysql username> <mysql password> <database name>`.
    - Uses the `cities` relationship for all `State` objects.
19. [101-relationship_states_cities_list.py](./101-relationship_states_cities_list.py)
    - Python script that uses SQLAlchemy to list all `State` and corresponding `City` objects in the database `hbtn_0e_101_usa`.
    - Usage: `./101-relationship_states_cities_list.py <mysql username> <mysql password> <database name>`.
    - Uses the `cities` relationship for all `State` objects.
    - Results are sorted by ascending `states.id` and `cities.id`.
20. [102-relationship_cities_states_list.py](./102-relationship_cities_states_list.py)
    - Python script that uses SQLAlchemy to list all `City` objects from the database `hbtn_0e_101_usa`.
    - Usage: `./102-relationship_cities_states_list.py <mysql username> <mysql password> <database name>`.
    - Uses the `state` relationship to access the `State` objects linked to `City` objects.
    - Results are sorted by ascending `cities.id`.
