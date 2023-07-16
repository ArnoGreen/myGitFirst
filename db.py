import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1',user='root',password='delicious',database='mydjango0503',auth_plugin='mysql_native_password')
cursor = conn.cursor()

