#!/usr/bin/python3

"""
A Script that lists all states from the database hbtn_0e_0_usa:
Requirements:
    -Your script should take 3 arguments: mysql username, mysql
    password and database name (no argument validation needed)
    -You must use the module MySQLdb (import MySQLdb)
    -Your script should connect to a MySQL server running on
    localhost at port 3306
    -Results must be sorted in ascending order by states.id
    -Results must be displayed as they are in the example below
    -Your code should not be executed when imported
"""

import sys
import MySQLdb


if __name__=='__main__':
    """
    script that Connect to the Database and fetches
    information from states.id
    """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    # get the cursor to interact with DB
    cur=db.cursor()

    # query to retrieve all states ordered by id
    cur.execute('SELECT * FROM states ORDER BY states.id ASC')

    # retrieve rows
    rows=cur.fetchall()

    for row in rows:
        print(row)

    # close cursor and DB
    cur.close()
    db.close()

