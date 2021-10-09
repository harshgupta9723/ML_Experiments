'''Aim of this script is to perform functions of a calculator such as addition, difference, multiplication and division.'''

from logging import error
from flask import Flask, request, jsonify
import db
from db import CalcDb

app = Flask(__name__)

#Functions of a calculator
class CalcFunctions :

    def add(self, a, b):

        if a and b is None:
            raise TypeError('Values cannot be None')  
        if type(a) and type(b) not in [float, int]: 
            raise TypeError('values can only be a valid integer or float') 
        sum = a + b
        return sum

    def diff(self, a, b):
        if a and b is None:
            raise TypeError('Values cannot be None')  
        if type(a) and type(b) not in [float, int]: 
            raise TypeError('values can only be a valid integer or float') 
        sub = a - b
        return sub

    def multiply(self, a, b):
        if a and b is None:
            raise TypeError('Values cannot be None')  
        if type(a) and type(b) not in [float, int]: 
            raise TypeError('values can only be a valid integer or float') 
        ml = a * b
        return ml
            
    def div(self, a, b):
        if a and b is None:
            raise TypeError('Values cannot be None')  
        if type(a) and type(b) not in [float, int]: 
            raise TypeError('values can only be a valid integer or float')
        if b == 0:
            raise TypeError('Can\'t divide with a zero')
        if a < 0 or b < 0 :
            raise TypeError('Values can\'t be negative')      
        div = a / b 
        return div

#Different routes to get the user response
@app.route('/', methods = ['GET'])
def home():
    return 'Calculator API'

@app.route('/add/', methods = ['GET','POST'])
def addition():

    x = request.form.get('x')
    y = request.form.get('y')
    try :
        sum = CalcFunctions().add(float(x), float(y))
    except TypeError as e :
        print(e)
    
    return jsonify({
        "sum" : sum
    })

@app.route('/diff/', methods = ['GET','POST'])
def difference():
    x = request.form.get('x')
    y = request.form.get('y')
    dif = CalcFunctions().diff(float(x), float(y))
    return jsonify({
        "difference" : dif
    })

@app.route('/multiply/', methods = ['GET','POST'])
def multiplication():
    x = request.form.get('x')
    y = request.form.get('y')
    multi = CalcFunctions().multiply(float(x), float(y))
    return jsonify({
        "multiplication" : multi
    })

@app.route('/divide/', methods = ['GET','POST'])
def division():
    x = request.form.get('x')
    y = request.form.get('y')
    divide = CalcFunctions().div(float(x), float(y))
    return jsonify({
        "division" : divide
    })

if __name__ == '__main__' :
    app.run()