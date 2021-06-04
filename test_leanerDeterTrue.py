import unittest
import scipy.stats
import numpy as np

class Test_test_leanerDeterTrue(unittest.TestCase):
    def test_A(self):
        X_arr=[[5, 15, 25, 35, 45, 55],[5,10,25,55],[0.5, 0.57, 0.89, 1, 2, 4]]
        Y_arr=[[5, 20, 14, 32, 22, 38],[1,6,22,30],[0.01, 0.27, 0.89, 1, 1.3, 2]]

        leanerDetermianation=[0.71588,0.89194, 0.99864]
        
        x=[]
        y=[]

        for i in range(len(X_arr)):
            for j in X_arr:  
                x.append(j)      
                for j in Y_arr:      
                    y.append(j)           
            r_lin, p = scipy.stats.pearsonr(x[i], y[i])
            r2_lin=round(r_lin**2,5)

            for i in range(len(leanerDetermianation)):
                if r2_lin==leanerDetermianation[i]:
                   correct = True

                self.assertTrue(correct)
if __name__ == '__main__':
    unittest.main()
