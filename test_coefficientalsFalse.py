import unittest
import numpy as np

class Test_test_coefficientalsFalse(unittest.TestCase):
    def test_A(self):
        x=[[1, 2, 3, 4, 5, 6],[1,2,3,4]]
        y=[[1,4,9,16,25,36],[0,3,8,15]]        
        coeff=['(2.0)x² + (-0.0)x + (0.0)','(1.0)x² + (1.0)x + (0.0)']
        for i in range(len(x)):
            arr = np.polyfit(x[i], y[i], 2)
            model='('+str(round(arr[0],5))+')x² + ('+str(round(arr[1],5))+')x + ('+str(round(arr[2],5))+')'
            if(coeff[i]==model):
                correct = True
            else: 
                correct = False
        self.assertFalse(correct)

if __name__ == '__main__':
    unittest.main()
