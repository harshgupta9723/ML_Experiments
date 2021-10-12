import requests
from flask import request
import json
import calculator, db
from calculator import CalcFunctions
from db import CalcDb

class client_calculator :

    def cl_add(self):

        url = "http://127.0.0.1:5000/add"
        x = 17
        y = 14
        r = requests.post(url, data = {'x' : x, 'y' : y})
        res = json.loads(r.text)
        sum = float(res['sum'])
        CalcDb().add_db(x, y, sum)

    def cl_diff(self):

        url = "http://127.0.0.1:5000/diff"
        x = 10
        y = 25
        r = requests.post(url, data = {'x' : x, 'y' : y})
        res = json.loads(r.text)
        diff = int(res['difference'])
        CalcDb().diff_db(x, y, diff)

    def cl_multiply(self):

        url = "http://127.0.0.1:5000/multiply"
        x = 56
        y = 7
        r = requests.post(url, data = {'x' : x, 'y' : y})
        res = json.loads(r.text)
        multi = int(res['multiplication'])
        CalcDb().multiply_db(x, y, multi)

    def cl_div(self):

        url = "http://127.0.0.1:5000/divide"
        x = 10
        y = 12
        r = requests.post(url, data = {'x' : x, 'y' : y})
        res = json.loads(r.text)
        div = float(res['division'])
        CalcDb().div_db(x, y, div)        

cl = client_calculator()
cl.cl_div()