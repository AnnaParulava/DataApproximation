
import scipy.stats

X_arr=[5, 15, 25, 35, 45, 55]
Y_arr=[5, 20, 14, 32, 22, 38]

leanerCorrelation=[0.84609,0.94443]
        
x=[]
y=[]

for X_arr,Y_arr in X_arr,Y_arr:
     x.append(X_arr)  
     y.append(Y_arr)   
     print(x)
     print(y)
         #r_lin, p = scipy.stats.pearsonr(x, y)
         #print(r_lin)











##import numpy as np
##from sklearn.linear_model import LinearRegression
##import matplotlib.pyplot as plt
##import scipy.stats
##from sklearn.preprocessing import PolynomialFeatures

#import operator
#import math
#import numpy as np
#import matplotlib.pyplot as plt

#from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error, r2_score
#from sklearn.preprocessing import PolynomialFeatures
#import scipy.stats
#import statistics

#x = np.array([5, 15, 25, 35, 45, 5.5])
#y = np.array([5, 20, 14, 32, 22, 38])


####### Линейная регрессия ##########

##Вывод уравнения регрессии
#LeanerModel = np.poly1d(np.polyfit(x, y, 1))
#print(LeanerModel)

##Вычисление коэффициента корреляции
#r_lin, p = scipy.stats.pearsonr(x, y)
#print("coefficient of correlation: ", r_lin)

##Вычисление коэффициента детерминации 1 способ
#x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
#model = LinearRegression().fit(x, y)
#r2_lin = model.score(x, y)
#print('coefficient of determination:', r2_lin)

##Вычисление коэффициента детерминации 2 способ
#print('coefficient of determination:', pow(r_lin,2))


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

##Вычисление коэффициента детерминации 2 способ
#x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
#polynomial_features= PolynomialFeatures(degree=2)
#x_poly = polynomial_features.fit_transform(x)

#model = LinearRegression()
#model.fit(x_poly, y)
#y_poly_pred = model.predict(x_poly)

#r2 = r2_score(y,y_poly_pred)
#print('coefficient of determination:', r2) 

##Вычисление коэффициента корреляции
#r=pow(r2,0.5)
#print("coefficient of correlation: ",r)
           















################
##polynomial_features= PolynomialFeatures(degree=2)
##x_poly = polynomial_features.fit_transform(x)

##model = LinearRegression()
##model.fit(x_poly, y)
##y_poly_pred = model.predict(x_poly)

##rmse = np.sqrt(mean_squared_error(y,y_poly_pred))
##r2 = r2_score(y,y_poly_pred)
##print(rmse)
##print(r2) #детерминация

##############
##fit2 = np.polyfit(x, y, 2)  
##v2 = np.polyval(fit2, x)
##mse2 = np.mean(np.square(y - v2))
##print(mse2)
##np.corrcoef(x, y)

################
##детерминация
##model = np.poly1d(np.polyfit(x, y, 2))
##print(model)
##print(r2_score(y, model(x)))


##корреляция квадратичной
##model = np.poly1d(np.polyfit(x, y, 2))
##print(model)
##r=r2_score(y, model(x))
##print(pow(r,0.5))






##poly = PolynomialFeatures(degree = 4)
##X_poly = poly.fit_transform(x)
##X_poly
##poly.fit(X_poly, y)
##lin2 = LinearRegression()
##lin2.fit(X_poly, y)
##plt.scatter(x, y, color = 'blue')

  

##plt.plot(X, lin.predict(X), color = 'red')

##plt.title('Linear Regression')

##plt.xlabel('Temperature')
##plt.ylabel('Pressure')

##plt.show()












##import numpy as np
##from sklearn.linear_model import LinearRegression
##import matplotlib.pyplot as plt
##import scipy.stats

##x = np.array([5, 15, 25, 35, 45, 55])
##y = np.array([5, 20, 14, 32, 22, 38])
##r, p = scipy.stats.pearsonr(x, y)
##print("corr:", r)

##x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
##model = LinearRegression().fit(x, y)
##r_sq = model.score(x, y)
##print('coefficient of determination:', r_sq)




###np.random.seed(777)

###X = 2*np.arange(30) + 5*np.random.beta(1, 2, 30)
###Y = 0.7*np.arange(30) + 2*np.random.randn(30)


###fig, ax = plt.subplots()

###ax.scatter(X, Y)

###ax.set_xlabel(r'Величина $\mathbf{X}$')
###ax.set_ylabel(r'Величина $\mathbf{Y}$')

###ax.set_title('Наблюдаемые значения двух величин')

###plt.show()

###VAL = np.vstack((X, Y))

###R_xy = np.corrcoef(VAL)
###R_xy