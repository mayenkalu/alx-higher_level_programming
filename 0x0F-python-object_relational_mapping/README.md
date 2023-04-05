# Python - Object Relational Mapping :page_with_curl: 
This project explores the concept of [Object Relational Mapping](https://www.fullstackpython.com/object-relational-mappers-orms.html). 
ORM is a special tool that connects two things - an object-oriented programming language and a relational database. It provides a way to store and retrieve data from a database using the programming language's objects, rather than writing complex SQL queries. This makes it easier for developers to work with databases and allows them to focus on the application logic instead of database management.
ORM helps take the information in the database and turn it into objects that can be used in the programming language. This makes it easier for developers to work with the information and focus on building the program, rather than worrying about managing the database. 

## Objectives :bulb:
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
    - Script lists all states in the database `hbtn_0e_0_usa`.
    - Takes 3 argument `<mysql username> <mysql password>  <database name>`.
    - Must use the module `MySQLdb (import MySQLdb)`.
    - Script should connect to a MySQL server running on `localhost` at port `3306`
    - Results of `states.id` ASC.

2. [1-filter_states.py](./1-filter_states.py)
    - Script lists all states with names starting with `N` in the database `hbtn_0e_0_usa`. 
    - same conditions in [0-select_states.py](./0-select_states.py).

3. [2-my_filter_states.py](./2-my_filter_states.py) 
    - Script displays all values matching a given name in the `states` table of the database `hbtn_0e_0_usa`.
    - Takes 4 arguments `<mysql username> <mysql password> <database name> <state name searched>`.
    - Use `format` to create the SQL query with user input.
    - Same conditions in [0-select_states.py](./0-select_states.py).

4. [3-my_safe_filter_states.py](./3-my_safe_filter_states.py) 
    - Script displays all values in the `states` table of the database `hbtn_0e_0_usa` where `name` matches artgument.
    - Same conditions in [2-my_filter_states.py](./2-my_filter_states.py).
    - This is an SQL Injection.

5.  [4-cities_by_state.py](./4-cities_by_state.py) 
    - Script lists all cities from the database `hbtn_0e_4_usa`.
    - Same conditions in [0-select_states.py](./0-select_states.py) but `cities.id` ASC.
    - Use `execute()` only once.

6.  [5-filter_cities.py](./5-filter_cities.py)
    - Script takes an argument in the name of a state and lists all cities in the database `hbtn_0e_4_usa`.
    - Same conditions in [4-cities_by_state.py](./4-cities_by_state.py).

6.  [model_state.py](./model_state.py) 
    - Python module defining a class `State` that inherits from `Base` and links to the MySQL table `states`.
    - Class attributes `id` and `name`.
    - Must be imported before calling `Base.metadata.create_all(engine)`.
    - Must use SQLAlchemy module.

7.  [7-model_state_fetch_all.py](./7-model_state_fetch_all.py)
    - Script listds all `State` objects from the database `hbtn_0e_6_usa`.
    - Must use the module SQLAlchemy.
    - Must import `State` and `Base` from `model_state - from model_state import Base, State`.
    - Conditions same in [0-select_states.py](./0-select_states.py).

8.  [8-model_state_fetch_first.py](./8-model_state_fetch_first.py)
    - Script prints the first `State` object from the database `hbtn_0e_6_usa`, ordered by `states.id`.
    - Conditions same in [7-model_state_fetch_all.py](./7-model_state_fetch_all.py).
    - If the `states` table is empty, prints `Nothing`.

9.  [9-model_state_filter_a.py](./9-model_state_filter_a.py)
    - Script lists all `State` objects that contain the letter `a` in the database `hbtn_0e_6_usa`.
    - Conditions same in [7-model_state_fetch_all.py](./7-model_state_fetch_all.py).
    - If no state has the name you searched for, display `Not found`.

10. [10-model_state_my_get.py](./10-model_state_my_get.py)
    - Script prints the `id` of the `State` object with name matching that passed as argument in the database `hbtn_0e_6_usa`.
    - Usage: `./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state searched name>`.
    - Displays the `id` of the matched `State`.
    - If no match is found, prints `Not found`.

11. [11-model_state_insert.py](./11-model_state_insert.py)
    - Python script that uses SQLAlchemy to add the `State` object "Louisiana" to the database `hbtn_0e_6_usa`.
    - Conditions same in [7-model_state_fetch_all.py](./7-model_state_fetch_all.py).
    - Prints the `id` of the new `State` after creation.

12. [12-model_state_update_id_2.py](./12-model_state_update_id_2.py)
    - Script changes the name of the `State` object with `id = 2` in the database `hbtn_0e_6_usa` to "New Mexico".
    - Conditions same in [7-model_state_fetch_all.py](./7-model_state_fetch_all.py).

13. [13-model_state_delete_a.py](./13-model_state_delete_a.py)
    - Script deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.
    - Conditions same in [7-model_state_fetch_all.py](./7-model_state_fetch_all.py).

14. [model_city.py](./model_city.py),
    [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py)
    - Module defines a class `City` that inherits from `Base` and links to the MySQL table `cities`.
    - Includes class attributes - `id` (cant be null, a primary key), `name` (cant be null, string of 128 characters) and `state_id` (cant be null, a foreign key to `states.id`).
    - Script lists all `City` objects in the database `hbtn_0e_14_usa`.
    - Conditions same in [7-model_state_fetch_all.py](./7-model_state_fetch_all.py).
    
15. [relationship_state.py](./relationship_state.py),
    [relationship_city.py](./relationship_city.py),
    [100-relationship_states_cities.py](./100-relationship_states_cities.py)
    - Improve the files `model_city.py` and `model_state.py`, and save them as `relationship_city.py` and `relationship_state.py`.
    - No change in `City` class.
    - In `State` class: the class attribute `cities` must represent a relationship with the class `City`. If the `State` object is deleted, all linked `City` objects are deleted. Also, the reference from a `City` object to his `State` should be named `state`                                                    
    - Script creates the `State` "California" with `City` "San Francisco" to the database `hbtn_0e_100_usa`.
    - Conditions same in [7-model_state_fetch_all.py](./7-model_state_fetch_all.py).

16. [101-relationship_states_cities_list.py](./101-relationship_states_cities_list.py)
    - Script lists all `State` and corresponding `City` objects in the database `hbtn_0e_101_usa`.
    - Conditions same in [7-model_state_fetch_all.py](./7-model_state_fetch_all.py).

17. [102-relationship_cities_states_list.py](./102-relationship_cities_states_list.py)
    - Script lists all `City` objects from the database `hbtn_0e_101_usa`.
    - Conditions same in [7-model_state_fetch_all.py](./7-model_state_fetch_all.py).
    - Must use only one query to the database.
    - Must use the `state` relationship to access to the `State` object linked to the `City` object.
