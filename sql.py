# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",                # Localhost for local connection
  user ="user",
  passwd ="password"
)

print(dataBase)
 
# Disconnecting from the server
dataBase.close()