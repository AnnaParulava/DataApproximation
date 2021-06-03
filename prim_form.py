from bottle import post, request, template
import re
import pdb
import json
import os
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import scipy.stats
from sklearn.metrics import mean_squared_error, r2_score
import scipy.stats
import statistics

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

       ###### Линейная регрессия ##########

        #Вывод уравнения регрессии
        LeanerModel = np.poly1d(np.polyfit(x, y, 1))
        print(LeanerModel)

        #Вычисление коэффициента корреляции
        r_lin, p = scipy.stats.pearsonr(x, y)
        print("coefficient of correlation: ", r_lin)

        #Вычисление коэффициента детерминации 
        x = np.array(x).reshape((-1, 1))
        model = LinearRegression().fit(x, y)
        r2_lin = model.score(x, y)
        print('coefficient of determination:', r2_lin)



        ####### Квадратичная регрессия ##########
        #x = np.array([5, 15, 25, 35, 45, 55])
        #arr = np.polyfit(x, y, 2)
        #model='('+str(round(arr[0],5))+')x² + ('+str(round(arr[1],5))+')x + ('+str(round(arr[2],5))+')'
        #print(model) 

        ##Вычисление коэффициента детерминации 1 способ
        #x = np.array([5, 15, 25, 35, 45, 55])
        #model = np.poly1d(np.polyfit(x, y, 2))
        #print(model)                                             #Вывод уравнения регрессии
        #r2_sq= r2_score(y, model(x))
        #print('coefficient of determination:', r2_sq)            #Вывод коэффициента детерминации

        ##Вычисление коэффициента корреляции
        #r=pow(r2,0.5)
        #print("coefficient of correlation: ",r)

        #вывод ответа
        return template('prim.tpl', title='Regression', year=2021, linCorr=r_lin, linDeter=r2_lin)
        #with open('mas_weight.txt', 'w') as file:
        #    json.dump(r_sq, file)
        #file.close()
        #return json.dumps( r)
    else:
        return template('prim', rows=int(request.forms.get('num')),title='Prim', message='Prim`s algorithm', year=datetime.now().year, linCorr="", linDeter="")









#
#Ппивет, давно хотел сказать, что ты волчица, а я волк 
#Ну и того 
#Ты пояла
#Alex Wolf
