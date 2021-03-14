import unittest
import unittest.mock as mock
from unittest.mock import patch
import os
import sys

sys.path.append(os.path.abspath('../../'))
from app import getUserDB
import models

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
SCORE_EXPECED = "expectedScore"
SCORE_W = "scoreW"
USER_W = "userW"

INITIAL_USERNAME = 'user1'
INITIAL_USERNAME2 = 'user2'


class GetUserTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [{
            KEY_EXPECTED: ['user1', 'user2'],
            SCORE_EXPECED: [100, 100]
        }]
        self.failure_test_paramus = [
            #no adding correct Name
            {
                USER_W: ['user32', 'user6453', 'user101', 'user401'],
                SCORE_W: [101, 3, 4, 10, 81]
            },
            #no adding the name, len should be wrong and index[2] too
            {
                USER_W: ['user45', 'user09', 'user3'],
                SCORE_W: [9, 1, 108, 86, 23]
            },
            #
            {
                USER_W: ['user667', 'user54', 'user32'],
                SCORE_W: [0, 156, 65, 867]
            }
        ]

        initial_person = models.Person(username=INITIAL_USERNAME, score=100)
        initial_person2 = models.Person(username=INITIAL_USERNAME2, score=100)
        self.initial_db_mock = [initial_person]
        self.initial_db_mock.append(initial_person2)

    def mocked_person_query_all(self):
        return self.initial_db_mock

    #this is the actual test
    def test_success(self):
        for test in self.success_test_params:
            with patch('models.Person.query') as mocked_query:
                mocked_query.all = self.mocked_person_query_all
                print(self.initial_db_mock)

                actual_userLResult, actual_scoresLResult = getUserDB()
                print(actual_userLResult)
                print(actual_scoresLResult)
                expected_userLResult = test[KEY_EXPECTED]
                expected_scoreLResult = test[SCORE_EXPECED]
                print(self.initial_db_mock)
                print(expected_userLResult)
                print(expected_scoreLResult)
                self.assertEqual(len(actual_userLResult),
                                 len(expected_userLResult))
                self.assertEqual(len(actual_scoresLResult),
                                 len(expected_scoreLResult))
                self.assertEqual(len(actual_userLResult),
                                 len(expected_scoreLResult))
                self.assertEqual(len(actual_scoresLResult),
                                 len(expected_userLResult))
                self.assertEqual(actual_userLResult[0],
                                 expected_userLResult[0])
                self.assertEqual(actual_userLResult[1],
                                 expected_userLResult[1])
                self.assertEqual(actual_scoresLResult[0],
                                 expected_scoreLResult[0])
                self.assertEqual(actual_scoresLResult[1],
                                 expected_scoreLResult[1])

    def test_failure(self):
        for test in self.failure_test_paramus:
            with patch('models.Person.query') as mocked_query:
                mocked_query.all = self.mocked_person_query_all
                print(self.initial_db_mock)
                actual_userLResult, actual_scoresLResult = getUserDB()
                print(actual_userLResult)
                print(actual_scoresLResult)
                userLResult2 = test[USER_W]
                scoreLResult2 = test[SCORE_W]
                print(self.initial_db_mock)
                print(userLResult2)
                print(scoreLResult2)
                self.assertNotEqual(len(actual_userLResult), len(userLResult2))
                self.assertNotEqual(len(actual_scoresLResult),
                                    len(scoreLResult2))
                self.assertNotEqual(actual_userLResult[0], userLResult2[0])
                self.assertNotEqual(actual_userLResult[1], userLResult2[1])
                self.assertNotEqual(actual_scoresLResult[0], scoreLResult2[0])
                self.assertNotEqual(actual_scoresLResult[1], scoreLResult2[1])


if __name__ == '__main__':
    unittest.main()
