#!/usr/bin/python3
import cgitb
cgitb.enable()
# Print necessary headers.
print("Content-Type: text/html")
print()
import pymysql
import cgitb
import cgi
#Haalt gegevens op uit get request
form = cgi.FieldStorage()
comment = form.getvalue("comment")
name = form.getvalue("username")
email = form.getvalue("email")

#connect met database
conn = pymysql.connect(
    db="pad",
    user="pad",
    passwd="Cybersec2021",
    host='db',)
c = conn.cursor()

#insert de gegevens in de aangegeven database
insert = """INSERT INTO `pad`.`form_requests` (`idform_requests`, `form_comment`, `form_email`, `form_name`) VALUES (0, %s, %s, %s);"""
insert_val = (comment, email, name)
c.execute(insert, insert_val)
conn.commit()

select = "SELECT * FROM `form_requests` WHERE `form_name`=%s"
c.execute(select, (name))
results = c.fetchall()
for r in results:
    print(r"\n")