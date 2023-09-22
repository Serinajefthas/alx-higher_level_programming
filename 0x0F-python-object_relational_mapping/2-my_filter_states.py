#!/usr/bin/python3
"""List all states with same name as user input from hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port='3306', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}'
                   ORDER BY states.id".format(str(sys.argv[4])))

    rows = cursor.fetchall()
    for i in rows:
        print(row)

    cursor.close()
    db.close()
