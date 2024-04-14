#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(searched))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
