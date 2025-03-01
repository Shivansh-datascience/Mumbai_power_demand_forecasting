import pymysql
import  mysql.connector as mysql_connection
import pandas as pd
import os

#fetching the Database credentials for environmen file
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME") 
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_SERVER = os.getenv("MYSQL_SERVER")
MYSQL_PORT = os.getenv("MYSQl_PORT")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

#checking the Database credentials by creating an list
Database_credentials = [
    MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_SERVER,MYSQL_PORT,MYSQL_DATABASE
                        ]
if all(Database_credentials):
    print(" Database credentials is imported")
else:
    print(" Database credentials not imported")

#making an connection to database with its credentials
Connection = pymysql.connect(
    host=MYSQL_SERVER,port=int(MYSQL_PORT),database=MYSQL_DATABASE,
    user=MYSQL_USERNAME,password=MYSQL_PASSWORD)
if Connection:
    print("Database connected successfully")
else:
    print("Database not connected successfully")


#creating an cursor object for reading and SQL Query
cursor_connection = Connection.cursor()
if cursor_connection:
    sql_statement = "SELECT * FROM long_data_ WHERE States = 'Maharashtra'"
    cursor_connection.execute(sql_statement)
    result = cursor_connection.fetchall()
    desc = [desc[0] for desc in cursor_connection.description]
    Connection.commit()
    cursor_connection.close()

#converting the reuslt into pandas dataframe
try:
    demand_forecasting_df = pd.DataFrame(result,columns=desc)
except Exception as e:
    print("error : {e}")
finally:
    print(demand_forecasting_df)


#saving these dataframe into folder structure
demand_forecasting_df.to_csv('dataset.csv')


