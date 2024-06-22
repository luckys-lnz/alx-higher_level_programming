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

    # Argument to be checked
    stateName=sys.argv[4]

    connector = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    
    # create cursor object - execute queries
    cur = connector.cursor()

    # execute sql query
    query = """
             SELECT *
             FROM states
             WHERE BINARY name = %s
             ORDER BY id ASC
             """
    cur.execute(query, (stateName,))

    # fetch results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # close connections
    cur.close()
    connector.close()
