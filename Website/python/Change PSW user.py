import pymysql

conn = pymysql.connect(
    db=fundementals.db_database,
    user=fundementals.db_user,
    passwd=fundementals.db_password,
    host='localhost',
    port=3306)
c = conn.cursor()