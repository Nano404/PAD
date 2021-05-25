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

conn = pymysql.connect(
    db="pad",
    user="pad",
    passwd="Cybersec2021",
    host='localhost',
    port=3306)
c = conn.cursor()

form = cgi.FieldStorage()
ip = form.getvalue("ip")

select = "SELECT * FROM `ipban` WHERE `ip` = " + ip
c.execute(select)
conn.commit()

if c.fetchone():
    print("ip banned")
else:
    sql = "INSERT INTO 'ipban' (`ip`) VALUES (%s)"
    val = ip
    c.execute(sql, val)
    conn.commit()
    print("ip banned")






