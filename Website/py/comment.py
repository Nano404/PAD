#!/usr/bin/python
# Import modules for CGI handling
import cgi, cgitb

# Import SQL Connector
import mysql.connector
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Start databate connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="W@chtw00rd123",
  database="CTF"
)

mycursor = mydb.cursor()

# Get data from fields, from html file
name = form.getvalue('name')
comment = form.getvalue('comment')
email = form.getvalue('email')

# Insert statement
sql = "INSERT INTO 'form requests' (`form_comment`, `form_email`, `form_name`) VALUES (%s, %s, %s)"
val = (comment, email, name)
mycursor.execute(sql, val)

mydb.commit()