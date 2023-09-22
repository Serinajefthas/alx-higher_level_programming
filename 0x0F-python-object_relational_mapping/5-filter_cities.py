#!/usr/bin/python3
"""List all cities of a state as an arg from db hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port='3306', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states ON
                   cities.state_id = states.id WHERE states.name=%s",
                   (sys.argv[4], ))

    rows = cursor.fetchall()
    for i in rows:
        print(row)

    cursor.close()
    db.close()
