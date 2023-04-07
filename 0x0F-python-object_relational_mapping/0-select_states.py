#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close() 
    
    """
-Import the MySQLdb module to allow the script to interact with the MySQL database.

-Import the argv function from the sys module to allow the script to receive input arguments from the command line.

-Check if the script is being run as the main program (as opposed to being imported as a module).

-Create a connection to the MySQL database using the input arguments for the host, port, username, password, database name, and character set.

-Create a cursor object to allow the script to execute SQL statements and retrieve data from the database.

-Execute a SELECT statement that retrieves all rows from the "states" table and orders them by their "id" in ascending order.

-Use the fetchall() method to retrieve all of the rows returned by the SELECT statement. The fetchall() statement returns a list of tuples, 
where each tuple represents a row of the result set. Each tuple contains values for each column in the corresponding row of the "states" table.

-Iterate through the rows and print each one to the console.

-Close the cursor and database connection to clean up resources.
    """
