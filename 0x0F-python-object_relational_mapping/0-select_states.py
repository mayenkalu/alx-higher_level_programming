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
- Use MySQLdb module to interact with MySQL database.
- Import `argv` function from sys module to get
  input arguments from command line.
- Check if script is the main program.
- Create connection to MySQL db using input
  arguments for host, port, username, password,
  db name, and character set.
- Create cursor object to execute SQL statements
  and retrieve data from the db.
- Execute `SELECT` statement to retrieve all rows from
  "states" table and order them by "id" in ascending order.
- Use `fetchall()` method to retrieve all rows
  returned by `SELECT` statement as list of tuples.
- Iterate through rows and print each one to console.
- Close cursor and db connection to clean up resources.
"""
