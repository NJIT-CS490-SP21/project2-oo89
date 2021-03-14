'''
    unit_testsUnM3.py 
    This file test the addUsersScoresToLists function from App.py. 
    This function is in charge to return two lists, one with the user and the other one with the scores. 
    I make sure here that the lists the function return are correct and also in order. 

'''
import unittest
import os
import sys

sys.path.append(os.path.abspath('../../'))
from app import addUsersScoresToLists

KEY_INPUT = "input"
KEY_EXPECTED_USERS = "expectedUSers"
KEY_EXPECTED_SCORES = "excpectedScores"


class TestAppListUS(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [{
            KEY_INPUT: {
                'Oscar': 119,
                'User1': 102,
                'Test1': 100,
                'Susy': 96,
                'Pepe': 84
            },
            KEY_EXPECTED_USERS: ['Oscar', 'User1', 'Test1', 'Susy', 'Pepe'],
            KEY_EXPECTED_SCORES: [119, 102, 100, 96, 84]
        }, {
            KEY_INPUT: {
                'Oscar': 119,
                'Pepe': 45,
                'Susy': 5,
                'User1': 3,
                'Test1': 1
            },
            KEY_EXPECTED_USERS: ['Oscar', 'Pepe', 'Susy', 'User1', 'Test1'],
            KEY_EXPECTED_SCORES: [119, 45, 5, 3, 1]
        }, {
            KEY_INPUT: {
                'User1': 5,
                'Pepe': 4,
                'Oscar': 3,
                'Susy': 2,
                'Test1': 1
            },
            KEY_EXPECTED_USERS: ['User1', 'Pepe', 'Oscar', 'Susy', 'Test1'],
            KEY_EXPECTED_SCORES: [5, 4, 3, 2, 1]
        }]
        self.failure_test_paramus = [{
            KEY_INPUT: {
                'Oscar': 119,
                'User1': 102,
                'Test1': 100,
                'Susy': 96,
                'Pepe': 84
            },
            KEY_EXPECTED_USERS: ['Oscar', 'User1', 'Test1', 'Susy', 'Pepe'],
            KEY_EXPECTED_SCORES: [119, 102, 100, 96, 84, 200, 400]
        }, {
            KEY_INPUT: {
                'Oscar': 119,
                'Pepe': 45,
                'Susy': 5,
                'User1': 3,
                'Test1': 1
            },
            KEY_EXPECTED_USERS: ['Oscar', 'Pepe', 'Susy', 'User1', 'Test1'],
            KEY_EXPECTED_SCORES: [119, 45, 5, 3]
        }, {
            KEY_INPUT: {
                'User1': 5,
                'Pepe': 4,
                'Oscar': 3,
                'Susy': 2,
                'Test1': 1
            },
            KEY_EXPECTED_USERS: ['User1', 'Pepe', 'Oscar', 'Susy', 'Test1'],
            KEY_EXPECTED_SCORES: [5, 4, 3, 2, 1, 85]
        }]

    def tearDown(self):
        pass

    def test_addUsersScoresToLists(self):
        for test in self.success_test_params:
            actual_usersList, actual_scoreList = addUsersScoresToLists(
                test[KEY_INPUT])
            expected_usersList = test[KEY_EXPECTED_USERS]
            expected_scoreList = test[KEY_EXPECTED_SCORES]
            self.assertEqual(actual_usersList, expected_usersList)
            self.assertEqual(actual_scoreList, expected_scoreList)
            self.assertEqual(len(actual_usersList), len(actual_scoreList))
            self.assertEqual(len(actual_usersList), len(expected_scoreList))
            self.assertIn(test[KEY_INPUT]['Oscar'], test[KEY_EXPECTED_SCORES])

    #Failure tests
    def test_failure1(self):
        for test in self.failure_test_paramus:
            actual_usersList, actual_scoreList = addUsersScoresToLists(
                test[KEY_INPUT])
            expected_scoreList = test[KEY_EXPECTED_SCORES]
            self.assertNotEqual(actual_scoreList, expected_scoreList)
            self.assertNotEqual(len(actual_usersList), len(expected_scoreList))


if __name__ == '__main__':
    unittest.main()
