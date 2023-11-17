#!/usr/bin/python3
"""List all the states"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    #connect to the database
    conn=MySQLdb.connect(host="localhost", port=3306, charset="utf8",
            user=argv[1], passwd=argv[2], db=argv[3])
cur = conn.cursor()
cur.execute("SELECT * FROM states where REGEXP_LIKE(name,'^n');")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
