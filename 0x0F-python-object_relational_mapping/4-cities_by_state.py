#!/usr/bin/python3
"""
Write a script that lists all cities
from the database hbtn_0e_4_usa
"""


import sys
import MySQLdb

def dbConnect():
    link=MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            host="localhost",
            port=3306,
            charset="utf8"
            )
    exe=link.cursor()
    exe.execute("SELECT cities.id, cities.name, states.name\ 
            from cities JOIN states\ 
            WHERE states.id = cities.state_id\
            ORDER BY cities.id ASC")
    link.commit()
    result=exe.fetchall()
    for res in result:
        print(res)
    exe.close()
    link.close()

if __name__ == "__main__":
    dbConnect()
