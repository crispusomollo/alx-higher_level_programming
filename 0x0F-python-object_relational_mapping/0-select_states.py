#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    #connect to the database
    connection = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
            user=argv[1], passwd=argv[2], db=argv[3])
cursor = connection.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connection.close()
