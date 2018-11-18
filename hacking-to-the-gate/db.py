import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database = "hackathon",
  auth_plugin='mysql_native_password',
  
)
