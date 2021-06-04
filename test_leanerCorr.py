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

        for i in X_arr:
            for j in Y_arr:
                x.append(i)
                y.append(j)         
                r_lin, p = scipy.stats.pearsonr(x, y)
                for i in leanerCorrelation:
                    if r_lin==leanerCorrelationх[i]:
                        correct = True

        self.assertTrue(correct)

if __name__ == '__main__':
    unittest.main()
