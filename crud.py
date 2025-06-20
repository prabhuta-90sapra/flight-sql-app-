import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='nonapsps',
        auth_plugin='mysql_native_password',
        database = 'indigo'
   )
    mycursor = conn.cursor()
    print('Connection established')
except:
    print('Connection error')

# mycursor.execute("CREATE DATABASE indigo")
# conn.commit()

# mycursor.execute("""
 
  # CREATE TABLE airport(
    # airport_id INTEGER PRIMARY KEY,
    # code VARCHAR(10) NOT NULL,
    # city VARCHAR(50) NOT NULL,
    # name VARCHAR(255) NOT NULL
 # )
#""")
# conn.commit()

#inserting data into table
#mycursor.execute("""
  # INSERT INTO airport values
  # (1,'DEL','New Delhi','IGIA'),
  # (2,'CCU','Kolkata','NSCA'),
   #(3,'BOM','Mumbai','CSMA')
   
#""")
#conn.commit()

# search?retrieve
mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])

#update
mycursor.execute("""
UPDATE airport
SET city = 'Bombay'
WHERE airport_id = 3
""")
conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)

#delete
mycursor.execute("DELETE FROM airport WHERE airport_id = 3")
conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)








