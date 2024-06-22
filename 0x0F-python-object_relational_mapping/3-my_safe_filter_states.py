#!/usr/bin/python3
"""
Script that takes in arguments
and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    """
    script that connects to the database
    """

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # curssor for interacting with db
    cur = db.cursor()

    # argument to match
    match = sys.argv[4]

    # query to execute match
    cur.execute('SELECT * FROM states WHERE name LIKE %s', (match, ))

    # fetch all rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # close connection
    cur.close()
    db.close()
