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
    try:
        name = request.forms.get('subm')
        if(name != "Ok"):
            rows=int(request.forms.get('num'))
            x=[]
            y=[]
            for i in range(rows):
                x.append(float(request.forms.get('fieldX' +str(i))))
                y.append(float(request.forms.get('fieldY' + str(i))))

            print(x)
            print(y)

            ###### Линейная регрессия ##########

            #Вывод уравнения регрессии
            LeanerModel = np.poly1d(np.polyfit(x, y, 1))
            LeanerModel = 'y = ' + str(LeanerModel)
            print(LeanerModel)

            #Вычисление коэффициента корреляции
            r_lin, p = scipy.stats.pearsonr(x, y)
            print("coefficient of correlation: ", r_lin)

            #Вычисление коэффициента детерминации 
            x_resh = np.array(x).reshape((-1, 1))
            model = LinearRegression().fit(x_resh, y)
            r2_lin = model.score(x_resh, y)
            print('coefficient of determination:', r2_lin)



            ###### Квадратичная регрессия ##########
            arr = np.polyfit(x, y, 2)
            QuadraticModel='y = ('+str(round(arr[0],5))+')x² + ('+str(round(arr[1],5))+')x + ('+str(round(arr[2],5))+')'
            print(QuadraticModel) 

            #Вычисление коэффициента детерминации
            model = np.poly1d(np.polyfit(x, y, 2))
            print(model)                                             #Вывод уравнения регрессии
            r2_q= r2_score(y, model(x))
            print('coefficient of determination:', r2_q)            #Вывод коэффициента детерминации

            #Вычисление коэффициента корреляции
            r_q=pow(r2_q,0.5)
            print("coefficient of correlation: ", r_q)

            ша 

        #вывод ответа
        else:
             return template('prim.tpl', title='Regression', year=2021, LeanerModel=LeanerModel, linCorr=r_lin, linDeter=r2_lin, QuadraticModel=QuadraticModel, QuadraticCorr=r_q, QuadraticDeter=r2_q, row=rows, x=x,y=y)
         
    except Exception:
        return template('prim', rows=2, title='Prim', message='Prim`s algorithm', year=datetime.now().year, LeanerModel='', linCorr="", linDeter="", QuadraticModel="", QuadraticCorr="", QuadraticDeter="",row=0, x=[],y=[]) 

    finally:
        pass






#
#Ппивет, давно хотел сказать, что ты волчица, а я волк 
#Ну и того 
#Ты пояла
#Alex Wolf
