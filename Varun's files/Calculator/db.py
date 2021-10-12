'''Aim of this script is to store the values and the operation performed on them in the database.'''

import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'database_1'
)

cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS Calculator')
cursor.execute('CREATE TABLE Calculator (id INT AUTO_INCREMENT PRIMARY KEY, value_1 FLOAT, value_2 FLOAT, sum FLOAT, difference FLOAT, multiplication FLOAT, division FLOAT)')

class CalcDb :

    def add_db(self, x, y, sum) :
        cursor.execute('INSERT INTO Calculator(value_1, value_2, sum) VALUES(%s, %s, %s)', (x, y, sum))
        db.commit()

    def diff_db(self, x, y, diff) :
        cursor.execute('INSERT INTO Calculator(value_1, value_2, difference) VALUES(%s, %s, %s)', (x, y, diff))
        db.commit()

    def multiply_db(self, x, y, multiply) :
        cursor.execute('INSERT INTO Calculator(value_1, value_2, multiplication) VALUES(%s, %s, %s)', (x, y, multiply))
        db.commit()

    def div_db(self, x, y, divide) :
        cursor.execute('INSERT INTO Calculator(value_1, value_2, division) VALUES(%s, %s, %s)', (x, y, divide))
        db.commit()                    
