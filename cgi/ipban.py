#!/usr/bin/python3
# Print necessary headers.
print("Content-Type: text/html")
print()
import pymysql
import cgitb
import cgi
import os
import sys
cgitb.enable()

#connect met database
conn = pymysql.connect(
    db="pad",
    user="pad",
    passwd="Cybersec2021",
    host='db',
    port = 3306)
c = conn.cursor()

form = cgi.FieldStorage()
ip = form.getvalue("ip")

select = "SELECT * FROM `ip` WHERE `ip` = %s;"
c.execute(select, (ip))

# als het ip gevonden is voeg hem toe anders print dat hij al bestaat
for r in c.fetchall():
    if r == ip:
        print("ip banned already")
else:
    sql = "INSERT INTO `ip`(`id`, `ip`) VALUES (0, %s)"
    val = (ip)
    c.execute(sql, val)
    conn.commit()
    print("ip banned")