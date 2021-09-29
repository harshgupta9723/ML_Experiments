import mysql.connector

myDb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '****'
)

myCursor = myDb.cursor()

myCursor.execute('CREATE DATABASE database_1')
myDb.database = 'database_1'
myCursor.execute('CREATE TABLE Customer (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))')

sql = 'INSERT INTO Customer(name, address) VALUES (%s,%s)'
val = [
    ('Adam','Southampton st 7'),
    ('Michael', 'Valley 345'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989')
]

myCursor.executemany(sql,val)
myDb.commit()