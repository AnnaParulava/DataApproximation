from bottle import post, request, template
import re
import pdb
import json
import os
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import scipy.stats
import operator
import math
from sklearn.metrics import mean_squared_error, r2_score
from scipy.optimize import curve_fit

@post('/prim', method='post')
def prim_form():
    
    name = request.forms.get('subm')
    if(name != "Ok"):
        rows=int(request.forms.get('num'))
        x=[]
        y=[]
        #если ячейка пустая, то 0
        for i in range(rows):
            x.append(int(request.forms.get('fieldX' +str(i))))
            y.append(int(request.forms.get('fieldY' + str(i))))

        print(x)
        print(y)

        #корреляция
        r, p = scipy.stats.pearsonr(x, y)
        print("corr:", r)

        #детерминация
        x = np.array(x).reshape((-1, 1))
        model = LinearRegression().fit(x, y)
        r_sq = model.score(x, y)
        print('coefficient of determination:', r_sq)

        #вывод ответа
        return template('prim.tpl', title='Regression', year=2021, answer=r_sq)
        #with open('mas_weight.txt', 'w') as file:
        #    json.dump(r_sq, file)
        #file.close()
        #return json.dumps( r)
    else:
        return template('prim', rows=int(request.forms.get('num')),title='Prim', message='Prim`s algorithm', year=datetime.now().year, answer="")

@post('/task2', method='post')
def prim_form():
    try:
        name = request.forms.get('subm')
        if(name == "Calculate"):
            rows=int(request.forms.get('num'))
            x=[]
            y=[]
            for i in range(rows):
                x.append(float(request.forms.get('fieldX' +str(i))))
                y.append(float(request.forms.get('fieldY' + str(i))))

            print(x)
            print(y)

            arr = np.polyfit(x, y, 2)
            model='('+str(round(arr[0],5))+')x² + ('+str(round(arr[1],5))+')x + ('+str(round(arr[2],5))+')'
            #Вычисление коэффициента детерминации 1 способ
            model = np.poly1d(np.polyfit(x, y, 2))
            print(model) #Вывод уравнения регрессии
            r2_sq= r2_score(y, model(x))
            print('coefficient of determination:', r2_sq) #Вывод коэффициента детерминации
            
           
              #запись результата в файл
           with open('results_task2.txt', 'w') as file:
                 file.write('>Coefficients of the quadratic regression line: '+ '('+str(round(arr[0],5))+')x² + ('+str(round(arr[1],5))+')x + ('+str(round(arr[2],5))+')' +' Determinism coefficient R2:'+ str(r2_sq))
           file.close()

            return template('task2.tpl', title='Aproximation', year=2021, coefficients='('+str(round(arr[0],5))+')x² + ('+str(round(arr[1],5))+')x + ('+str(round(arr[2],5))+')', determinism = str(r2_sq),  row=rows, x=x,y=y)
        else:
            return template('task2.tpl', rows=int(request.forms.get('num')),title='task2', message='', year=datetime.now().year, coefficients="", determinism="", row=0, x=[],y=[] )
    except Exception:
        return template('task2.tpl', title='Aproximation', year=2021, coefficients='Введите значения', determinism='', row=0, x=[],y=[] )
        
    finally:
        pass
