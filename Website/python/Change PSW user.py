import pymysql
import cgitb
import cgi
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

conn = pymysql.connect(
    db="pad",
    user="pad",
    passwd="Cybersec2021",
    host='localhost',
    port=3306)
c = conn.cursor()

