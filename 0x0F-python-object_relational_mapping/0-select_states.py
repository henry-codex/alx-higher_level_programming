#!/usr/bin/env python3

'''Connect to the database'''
import MySQLdb
import sys

def mysqlconnect():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    try:
        db_connection = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM states")
        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Database Error:", e)

    finally:
        if db_connection:
            cursor.close()
            db_connection.close()

if __name__ == '__main__':
    mysqlconnect()
