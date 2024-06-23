#!/usr/bin/python3
"""
script that takes in the name of a state as
an argument and lists all cities of that state,
using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    """
    script that uses arguments to search for cities
    """
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # get cursor to iteract with DB
    cur = db.cursor()

    # query to search cities in states
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4], ))

    # fetch rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # close connections
    cur.close()
    db.close()
