import pymysql

conn = pymysql.connect(
    db=fundementals.database,
    user=fundementals.username,
    passwd=fundementals.password,
    host='localhost',
    port=3306)
c = conn.cursor()