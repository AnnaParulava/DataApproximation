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
    
    name = request.forms.get('subm')
    if(name != "Ok"):
        rows=int(request.forms.get('num'))
        x=[]
        y=[]
        #если ячейка пустая, то 0
        for i in range(rows):

            #if((request.forms.get('fieldX' + str(i))&&(request.forms.get('fieldY' + str(i)))))==""):
                #return template('task2', rows=int(request.forms.get('num')),title='task2', message='Prim`s algorithm', year=datetime.now().year, answer="Fill all boxes")
           # else:
            x.append(int(request.forms.get('fieldX' + str(i))))
            y.append(int(request.forms.get('fieldY' + str(i))))

        print(x)
        print(y)
        #sq_x = 0 #сумма квадратов иксов
        #third_x = 0 #сумма кубов иксов
        #fourth_x = 0 #сумма иксов в четвертой степени
        #sum_x = 0 #сумма иксов
        #sum_y = 0 #сумма игриков
        #sum_xy = 0 #сумма произведения x на y
        #sum_x2y = 0 #сумма произведения x^2 на y
        #n=len(x)
        #for i in range(len(x)):
        #    sq_x+=(1/x[i])*(1/x[i])
        #    third_x+=(1/x[i])**3
        #    fourth_x+=(1/x[i])**4
        #    sum_x+=(1/x[i])
        #    sum_y+=y[i]
        #    sum_xy+=y[i]*(1/x[i])
        #    sum_xy+=y[i]*(1/x[i])
        #print(sum_x,', ',sq_x,', ',third_x,', ',fourth_x)
        #A=np.array([[sq_x, third_x, fourth_x],[sum_x, sq_x, third_x],[n, sum_x, sq_x]])
        #B = np.array([ sum_x2y, sum_xy, sum_y])
        #np.linalg.solve(A, B)    
        arr = np.polyfit(x, y, 2)
        model='('+str(round(arr[0],5))+')x² + ('+str(round(arr[1],5))+')x + ('+str(round(arr[2],5))+')'
        #Вычисление коэффициента детерминации 1 способ
        model = np.poly1d(np.polyfit(x, y, 2))
        print(model) #Вывод уравнения регрессии
        r2_sq= r2_score(y, model(x))
        print('coefficient of determination:', r2_sq) #Вывод коэффициента детерминации
        

        return template('task2.tpl', title='Aproximation', year=2021, answer='Коэфиценты квадратичной линии регрессии: \n ('+str(round(arr[0],5))+')x² + ('+str(round(arr[1],5))+')x + ('+str(round(arr[2],5))+') Коэффициент детерминированности R2: '+ str(r2_sq))
    else:
        return template('task2', rows=int(request.forms.get('num')),title='task2', message='Prim`s algorithm', year=datetime.now().year, answer="")
