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


        #корреляция
        r, p = scipy.stats.pearsonr(x, y)
        print("corr:", r)

        #детерминация
        x = np.array(x).reshape((-1, 1))
        model = LinearRegression().fit(x, y)
        r_sq = model.score(x, y)
        print('coefficient of determination:', r_sq)

        #вывод ответа
        return template('task2.tpl', title='Aproximation', year=2021, answer=r_sq)
    else:
        return template('task2', rows=int(request.forms.get('num')),title='task2', message='Prim`s algorithm', year=datetime.now().year, answer="")








#
#Ппивет, давно хотел сказать, что ты волчица, а я волк 
#Ну и того 
#Ты пояла
#Alex Wolf
