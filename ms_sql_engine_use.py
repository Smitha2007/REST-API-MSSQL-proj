import sqlalchemy
from sqlalchemy.engine import URL

connection_string = "DRIVER={SQL Server Native Client 11.0};SERVER=LAPTOP-4PDJOMHL;DATABASE=Testdb;Trusted_Connection=yes"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

engine = sqlalchemy.create_engine(connection_url)

#engine = sqlalchemy.create_engine('mssql+pyodbc://LAPTOP-4PDJOMHL/Testdb ,DRIVER={SQL Server Native Client 11.0}, Trusted_Connection=yes')

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,100,size=(100, 8)), columns=list('ABCDEFGH')) 
#print(df)

sheet_1 = df[list('ABFH')] #df[['Col1', 'Col4', 'F', 'H']]
#print(sheet_1)

sheet_2 = df[list('CG')]
#print(sheet_2)

sheet_3 = df[list('DEF')]
#print(sheet_3)

sheet_4 = df[list('ACEG')]
#print(sheet_4)

# establishing the connection to the databse using engine as an interface
conn = engine.connect()

# printing names of the tables present in the database
print(engine.table_names())

# checking whether the connection was actually established by selecting and displaying contents of table from the database
result = engine.execute("select * from dummy")
for row in result:
    print (row)
result.close()

# reading a SQL query using pandas
sql_query = pd.read_sql_query('SELECT * FROM Testdb.dbo.dummy', engine)  #NOT WORKIN

# saving SQL table in a pandas data frame
df = pd.DataFrame(sql_query, columns = ['column1','column2'])

print(df)
'''
df = pd.read_csv(‘tablename’)
# create a new table and append data frame values to this table
df.to_sql(‘tablename’, con=engine, if_exists=’append’,index=False,chunksize=1000)
'''


sheet_1.to_sql('Group_1_table', engine) #Creates whole new table
#print(pd.read_sql('Group_1_table', engine))


conn.close()

#refer: https://medium.com/@anushkamehra16/connecting-to-sql-database-using-sqlalchemy-in-python-2be2cf883f85