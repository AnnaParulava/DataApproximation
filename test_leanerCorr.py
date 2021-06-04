import unittest
import scipy.stats

class Test_test_leanerCorr(unittest.TestCase):
    def test_A(self):
        #data={"1": [[5, 15, 25, 35, 45, 55], [5, 20, 14, 32, 22, 38]], "2": [[5,10,25,55], [1,6,22,30]]}
        #sum_d={"1":0.84609,"2":0.94443}

        X_arr=[[5, 15, 25, 35, 45, 55],[5,10,25,55]]
        Y_arr=[[5, 20, 14, 32, 22, 38],[1,6,22,30]]

        leanerCorrelation=[0.84609,0.94443]
        
        x=[]
        y=[]

        for X_arr in X_arr:
            for Y_arr in Y_arr:
                x.append(X_arr)
                y.append(Y_arr)         
                r_lin, p = scipy.stats.pearsonr(x, y)
                for leanerCorrelation in leanerCorrelation:
                    if r_lin==leanerCorrelation:
                        correct = True

        self.assertTrue(correct)

if __name__ == '__main__':
    unittest.main()
