#!/usr/bin/python3
"""
script that takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

script takes 4 arguments.
"""
import sys
import MySQLdb

if __name__=='__main__':
    """
    Script that connects to the Database
    """

    # connect to database
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Grab cursor to interact with db
    cur = db.cursor()

    # query that takes arguments
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))

    # fetch the all rows
    rows = cur.fetchall()

    # iterate rows
    for row in rows:
        print(row)

    # close connections
    cur.close()
    db.close()
