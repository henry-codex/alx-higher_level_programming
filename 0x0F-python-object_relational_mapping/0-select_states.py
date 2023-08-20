#!/usr/bin/env python3

'''Connect to the database and list all states'''

import MySQLdb
import sys

def list_states():
    db_connection = None

    try:
        # Connect to the MySQL server
        db_connection = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            host='localhost'
        )

        cursor = db_connection.cursor()

        # Execute the SELECT query to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()

        # Display the states
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Database Error:", e)

    finally:
        if db_connection:
            cursor.close()
            db_connection.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    list_states()
