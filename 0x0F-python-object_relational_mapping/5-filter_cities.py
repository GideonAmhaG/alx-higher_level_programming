#!/usr/bin/python3
"""module that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time, one that
is safe from MySQL injections!"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                 LEFT JOIN states ON cities.state_id = states.id
                 WHERE states.name = %s
                 ORDER BY cities.id ASC;""", (argv[4],))
    for row in cur.fetchall():
        print(", ".join(row[1]))
