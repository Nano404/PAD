#!/usr/bin/python3
# Print necessary headers.
print("Content-Type: text/html")
print()
import pymysql
import cgitb
import cgi
cgitb.enable()

form = cgi.FieldStorage()
comment = form.getvalue("comment")
name = form.getvalue("name")
email = form.getvalue("email")

conn = pymysql.connect(
    db="pad",
    user="pad",
    passwd="Cybersec2021",
    host='localhost',
    port=3306)
c = conn.cursor()


insert = """INSERT INTO `mydb`.`form requests` (`idform requests`, `form_comment`, `form_email`, `form_name`) VALUES (%s, %s, %s);"""
insert_val = (comment, email, name)
c.execute(insert, insert_val)

select = """SELECT * FROM `formrequests` WHERE `form_name` = " + name;"""
print("The following message has been sent{}".format(select))