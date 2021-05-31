
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import scipy.stats

x = np.array([5, 15, 25, 35, 45, 55])
y = np.array([5, 20, 14, 32, 22, 38])
r, p = scipy.stats.pearsonr(x, y)
print("corr:", r)

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)




#np.random.seed(777)

#X = 2*np.arange(30) + 5*np.random.beta(1, 2, 30)
#Y = 0.7*np.arange(30) + 2*np.random.randn(30)


#fig, ax = plt.subplots()

#ax.scatter(X, Y)

#ax.set_xlabel(r'Величина $\mathbf{X}$')
#ax.set_ylabel(r'Величина $\mathbf{Y}$')

#ax.set_title('Наблюдаемые значения двух величин')

#plt.show()

#VAL = np.vstack((X, Y))

#R_xy = np.corrcoef(VAL)
#R_xy