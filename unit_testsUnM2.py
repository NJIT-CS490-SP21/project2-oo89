'''
    unit_testsUnM2.py 
    This file test the sortDic function from App.py. 
    This function is in charge to return a sorted dictionary. 
    On this test, I make sure that the returned dictionary is correct 
    and the function works as it is supposed to work.    

'''
import unittest 
import os
import sys

sys.path.append(os.path.abspath('../../'))
from app import sortDic


KEY_INPUT = "input"
KEY_EXPECTED = "expected"

class TestAppSortDic(unittest.TestCase):
    
    def setUp(self): 
        self.success_test_params = [
                {
                    KEY_INPUT: {'Test1': 100, 'Susy': 96, 'Oscar': 119, 'Pepe': 84, 'User1': 102},
                    KEY_EXPECTED: {'Oscar': 119, 'User1': 102, 'Test1': 100, 'Susy': 96, 'Pepe': 84}
                },
                {
                    KEY_INPUT: {'Test1': 1, 'Susy': 5, 'Oscar': 119, 'Pepe': 45, 'User1': 3},
                    KEY_EXPECTED: {'Oscar': 119, 'Pepe': 45, 'Susy': 5, 'User1': 3, 'Test1': 1}
                },
                {
                    KEY_INPUT: {'Pepe': 4, 'Test1': 1, 'Susy': 2, 'Oscar': 3, 'User1': 5},
                    KEY_EXPECTED: {'User1': 5, 'Pepe': 4, 'Oscar': 3, 'Susy': 2, 'Test1': 1}
                }
                
            ]
        self.failure_test_paramus = [
               {
                    KEY_INPUT: {'Test1': 100, 'Susy': 96, 'Oscar': 119, 'Pepe': 84, 'User1': 102},
                    KEY_EXPECTED: {'Osrfcar': 1, 'User1': 102, 'Test1': 5, 'Susy': 96, 'Peytype': 884}
                },
                {
                    KEY_INPUT: {'Test1': 1, 'Susy': 5, 'Oscar': 119, 'Pepe': 45, 'User1': 3},
                    KEY_EXPECTED: {'Oscar': 119, 'Pegtpe': 345, 'Susy': 5, 'User1': 3, 'Test1': 120}
                },
                {
                    KEY_INPUT: {'Pepe': 4, 'Test1': 1, 'Susy': 2, 'Oscar': 3, 'User1': 5},
                    KEY_EXPECTED: {'User1': 1, 'Pepe': 4, 'Oscar': 3, 'S5fusy': 2, 'Test1': 5}
                }
            ]    
    def tearDown(self):
        pass 
    
    def test_sortDic(self):
        for test in self.success_test_params:
            actual_usersDicSorted = sortDic(test[KEY_INPUT])
            expected_dic = test[KEY_EXPECTED]
            self.assertEqual(actual_usersDicSorted, expected_dic)
            self.assertEqual(len(actual_usersDicSorted),len(expected_dic))
            self.assertEqual(test[KEY_EXPECTED]['Oscar'], actual_usersDicSorted['Oscar'])
   
    def test_scoreOrder(self):
        for test in self.success_test_params:
            actual_usersDicSorted = sortDic(test[KEY_INPUT])
            flag = 0
            i = 1
            tempList = []
            for val in actual_usersDicSorted.values():
                tempList.append(val)
            while i < len(tempList): 
                if(tempList[i] > tempList[i - 1]): 
                    flag = 1
                i += 1
            self.assertEqual(flag, 0)
    
    #Failure tests 
    def test_failure1(self):
        for test in self.failure_test_paramus:
            actual_usersDicSorted = sortDic(test[KEY_INPUT])
            expected_dic = test[KEY_EXPECTED]
            self.assertNotEqual(actual_usersDicSorted, expected_dic)
      
    
if __name__ == '__main__':
    unittest.main()