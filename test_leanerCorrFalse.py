import unittest
import scipy.stats
import numpy as np

class Test_test_leanerUncorr(unittest.TestCase):
    def test_A(self):
        X_arr=[[5, 15, 25, 35, 45, 55],[5,10,25,55],[0.5, 0.57, 0.89, 1, 2, 4]]
        Y_arr=[[5, 20, 14, 32, 22, 38],[1,6,22,30],[0.01, 0.27, 0.89, 1, 1.3, 2]]

        leanerCorrelation=[0.1, 0.1, 4]
        
        x=[]
        y=[]

        for i in range(len(X_arr)):
            for j in X_arr:  
                x.append(j)      
                for j in Y_arr:      
                    y.append(j)           
            r_lin, p = scipy.stats.pearsonr(x[i], y[i])

            r_lin=round(r_lin,5)

            for i in range(len(leanerCorrelation)):
                if r_lin!=leanerCorrelation[i]:
                   correct = False
                
                self.assertFalse(correct)

if __name__ == '__main__':
    unittest.main()
