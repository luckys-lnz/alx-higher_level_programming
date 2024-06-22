#!/usr/bin/python3
"""
script that lists all states with a name
starting with N (upper N) from the
database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username,
mysql password and database name
(no argument validation needed)

You must use the module MySQLdb (import MySQLdb)

Your script should connect to a
MySQL server running on localhost at port 3306

Results must be sorted in ascending order by states.id

Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """
    Script to list all states starting
    with the upper case (N)
    """
    db=MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    # get cursor to interact with DB
    cur=db.cursor()

    # query to to get states with upper case' N'
    cur.execute("""
            SELECT id,name
            FROM states
            WHERE name
            LIKE 'N%'
            ORDER BY id ASC
            """)

    #get the rows
    rows=cur.fetchall()

    # iterate through the rows to get states
    for row in rows:
        print(row)

    # Close cursor and DB
    cur.close()
    db.close()
