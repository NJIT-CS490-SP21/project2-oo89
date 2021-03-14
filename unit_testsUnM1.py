'''
    unit_testsUnM1.py 
    This file test the Profit function from App.py. This function is in charge to return a dictionary 
    where the key is the user name and the value is the amount of money that the user has won or lost. 
    This was calculated base on the $100 credit that was given to the user. If the number you see is 
    negative it means the user is losing money.  

'''
import unittest 
import os
import sys

sys.path.append(os.path.abspath('../../'))
from app import calculateProfit


KEY_INPUT_USERS = "input"
KEY_INPUT_SCORE = "expectedUSers"
KEY_EXPECTED_PROFIT = "excpectedScores"

class TestAppProfit(unittest.TestCase):
    
    def setUp(self): 
        self.success_test_params = [
                {
                    KEY_INPUT_USERS: ['Oscar', 'User1', 'Test1', 'Susy', 'Pepe'],
                    KEY_INPUT_SCORE: [150, 119, 100, 96, 84],
                    KEY_EXPECTED_PROFIT: {'Oscar': 50, 'User1': 19, 'Test1': 0, 'Susy': -4, 'Pepe': -16}
                },
                {
                    KEY_INPUT_USERS: ['Oscar2', 'User2', 'Test2', 'Susy2', 'Pepe2'],
                    KEY_INPUT_SCORE: [200, 150, 95, 90, 20],
                    KEY_EXPECTED_PROFIT: {'Oscar2': 100, 'User2': 50, 'Test2': -5, 'Susy2': -10, 'Pepe2': -20}
                },
                {
                    KEY_INPUT_USERS: ['Oscar3', 'User3', 'Test3', 'Susy3', 'Pepe3'],
                    KEY_INPUT_SCORE: [171, 156, 63, 29, 5],
                    KEY_EXPECTED_PROFIT: {'Oscar3': 71, 'User3': 56, 'Test3': -37, 'Susy3': -71, 'Pepe3': -95}
                }
                
            ]
        self.failure_test_paramus = [
                {
                    KEY_INPUT_USERS: ['Oscar', 'User1', 'Test1', 'Susy', 'Pepe'],
                    KEY_INPUT_SCORE: [150, 119, 100, 96, 84],
                    KEY_EXPECTED_PROFIT: {'Oscar': 2, 'User1': 19, 'Test1': 0, 'Susy': -4, 'Pepe': -16, 'Oscar2': -85}
                },
                {
                    KEY_INPUT_USERS: ['Oscar2', 'User2', 'Test2', 'Susy2', 'Pepe2'],
                    KEY_INPUT_SCORE: [200, 150, 95, 90, 20],
                    KEY_EXPECTED_PROFIT: {'Oscar2': 25, 'User2': 50}
                },
                {
                    KEY_INPUT_USERS: ['Oscar3', 'User3', 'Test3', 'Susy3', 'Pepe3'],
                    KEY_INPUT_SCORE: [171, 156, 63, 29, 5],
                    KEY_EXPECTED_PROFIT: {'Oscar3': 70, 'User3': 56, 'Test3': -37, 'Susy3': -71, 'Pepe3': -95, 'Pepe4': -95,'Pepe5': -95}
                }
            ]    
    def tearDown(self):
        pass 
    
    def test_profit(self):
        for test in self.success_test_params:
            actual_profit = calculateProfit(test[KEY_INPUT_USERS], test[KEY_INPUT_SCORE])
            expected_profit = test[KEY_EXPECTED_PROFIT]

            self.assertEqual(actual_profit, actual_profit)
            self.assertEqual(len(actual_profit),len(expected_profit))
    #Failure tests 
    def test_failure1(self):
        for test in self.failure_test_paramus:
            actual_profit = calculateProfit(test[KEY_INPUT_USERS], test[KEY_INPUT_SCORE])
            expected_profit = test[KEY_EXPECTED_PROFIT]

            self.assertNotEqual(actual_profit, expected_profit)
            self.assertNotEqual(len(actual_profit),len(expected_profit))
      
    
if __name__ == '__main__':
    unittest.main()