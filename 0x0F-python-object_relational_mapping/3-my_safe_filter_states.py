#!/usr/bin/python3
"""
return matching states; safe from MySQL injections
"""

import MySQLdb
import sys

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    # create cursor to execute queries using SQL
    cursor = db.cursor()
    sql_cmd = """SELECT *
                 FROM states
                 WHERE name=%s ORDER BY id ASC"""
    cursor.execute(sql_cmd, (sys.argv[4],))

    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
