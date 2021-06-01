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

@post('/Prim', method='post')
def prim_form():
    return template('prim', rows=int(request.forms.get('num')),title='Prim', message='Prim`s algorithm', year=datetime.now().year)

@post('/Primm', method='post')
def prim_form():
    
    rows=int(request.forms.get('num'))
    x=[]
    y=[]
    #если ячейка пустая, то 0
    for i in range(rows):
        x.append(int(request.forms.get('fieldX' +str(i))))
        y.append(int(request.forms.get('fieldY' + str(i))))
    print(x)
    print(y)

    #x = np.array([5, 15, 25, 35, 45, 55])
    #y = np.array([5, 20, 14, 32, 22, 38])
    r, p = scipy.stats.pearsonr(x, y)
    print("corr:", r)

    x = np.array(x).reshape((-1, 1))
    model = LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    print('coefficient of determination:', r_sq)

    with open('mas_weight.txt', 'w') as file:
        json.dump(r_sq, file)
    file.close()
    return json.dumps(r,r_sq)
#
#
#Ппивет, давно хотел сказать, что ты волчица, а я волк 
#Ну и того 
#Ты пояла
#Alex Wolf
