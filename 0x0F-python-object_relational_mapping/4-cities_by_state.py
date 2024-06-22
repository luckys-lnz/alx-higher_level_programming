#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
take 3 arguments: mysql username, mysql password and database name.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    """List all cities from DB"""
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # get cursor to interact with db
    cur = db.cursor()

    # query to sort city
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")

    # fetc all the rows
    rows = cur.fetchall()

    # iterate rows
    for row in rows:
        print(row)

    # close all connections
    cur.close()
    db.cursor()
