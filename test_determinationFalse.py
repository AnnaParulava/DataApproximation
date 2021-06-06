import unittest
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

class Test_test_determinationFalse(unittest.TestCase):
    def test_A(self):
        x=[[1, 2, 3, 4, 5, 6],[1,2,3,4]]
        y=[[1,4,9,16,25,36],[0,3,8,15]]
        deter=[0.5,0.9]
        for i in range(len(x)):
            model = np.poly1d(np.polyfit(x[i], y[i], 2))
            r2_sq= r2_score(y[i], model(x[i]))
            if(deter[i]==r2_sq):
                correct = True
            else: 
                correct = False
        self.assertFalse(correct)

if __name__ == '__main__':
    unittest.main()
