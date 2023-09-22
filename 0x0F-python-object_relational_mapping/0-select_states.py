#!/usr/bin/python3
"""List all states from db hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to mysql server
    sqlserver = MySQLdb.connect(host='localhost', port='3306', user=my
                                sql_username, passwd=mysql_password,
                                db=database_name)

    cursor = sqlserver.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    rows = cursor.fetchall()
    for i in rows:
        print(row)

    cursor.close()
    sqlserver.close()
