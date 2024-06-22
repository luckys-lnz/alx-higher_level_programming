#!/usr/bin/python3
"""
A script that prints the states starting
with uppercase 'N' in a database and ordered
by states.id. Also accepts 3 arguments
(password, username, dbname)
"""
import sys
import MySQLdb

if __name__=='__main__':
    """
    Script to connect and interact with database
    """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    # get cursor to interact with DB
    cur = db.cursor()

    #querey to grab states starting with 'N'
    cur.execute("""
        SELECT id,name
        FROM states
        WHERE name
        LIKE 'N%'
        ORDER BY states.id ASC
    """)

    # show all rows
    rows = cur.fetchall()

    #iterate rows in state table
    for row in rows:
        print(row)

    # close Cursor and DB
    cur.close()
    db.close()

