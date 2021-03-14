import unittest
import unittest.mock as mock
from unittest.mock import patch
import os
import sys

sys.path.append(os.path.abspath('../../'))
from app import getUserDB, addNewUserDB, updateWinnerLoser
import models

USER_EXPECTED = "input"
KEY_INPUT ="input"
KEY_EXPECTED = "expected"
SCORE_EXPECED = "expectedScore"
SCORE_W = "scoreW"
USER_W = "userW"

INITIAL_USERNAME = 'user1'
INITIAL_USERNAME2 = 'user2'

class UpdateWinnerLoser(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: ['user2','user1'],
                USER_EXPECTED: ['user2','user1'],
                SCORE_EXPECED: [101, 99]
            },
            {
                KEY_INPUT: ['user1','user2'],
                USER_EXPECTED: ['user1','user2'],
                SCORE_EXPECED: [100, 100]
            },
             {
                KEY_INPUT: ['user1','user2'], 
                USER_EXPECTED: ['user1','user2'],
                SCORE_EXPECED: [101, 99]
            },
            {
                KEY_INPUT: ['user1','user2'], 
                USER_EXPECTED: ['user1','user2'],
                SCORE_EXPECED: [102, 98]
            }
        ]
        
        initial_person = models.Person(username=INITIAL_USERNAME, score=100)
        initial_person2 = models.Person(username=INITIAL_USERNAME2, score=100)
        self.initial_db_mock = [initial_person]
        self.initial_db_mock.append(initial_person2)
        print(self.initial_db_mock)
    
    #this is called in test_success 
    def mocked_db_session_add(self, username):
        self.initial_db_mock.append(username)
        
    #to simulate commit to the db it also called in test_success 
    def mocked_db_session_commit(self):
        pass
    
    #this is called in test_success 
    def mocked_person_query_all(self):
        return self.initial_db_mock
        
    def mocked_db_session_query_winner(self):
        pass
        
    def mocked_db_session_query_losser(self):
        pass
        
    def mocked_db_w_score(self,winnerName):
        i = 0
        for name in self.initial_db_mock:
            if name.username == winnerName:
                print(name.username)
                self.initial_db_mock[i].score = self.initial_db_mock[i].score + 1
                print(name.score)
                break
            i +=1
        return self.initial_db_mock
        
    def mocked_db_l_score(self, losserName):
        i = 0
        for name in self.initial_db_mock:
            if name.username == losserName:
                print(name.username)
                self.initial_db_mock[i].score = self.initial_db_mock[i].score - 1
                print(name.score)
                break
            i +=1
        return self.initial_db_mock   
        
    #this is the actual test 
    def test_success(self):
        for test in self.success_test_params:
            with patch('app.db.session.query') as mocked_query:
                mocked_query.get = self.mocked_db_session_query_winner
                with patch('app.db.session.query') as mocked_query:
                    mocked_query.get = self.mocked_db_session_query_losser
                    self.mocked_db_w_score(test[KEY_INPUT][0])
                    self.mocked_db_l_score(test[KEY_INPUT][1])
                    with patch('app.db.session.commit', self.mocked_db_session_commit):
                        with patch('models.Person.query') as mocked_query:
                            mocked_query.all = self.mocked_person_query_all
                            actual_userLResult, actual_scoresLResult = updateWinnerLoser(test[KEY_INPUT][0], test[KEY_INPUT][1])
                            print('actual')
                            print(actual_userLResult)
                            print(actual_scoresLResult)
                            
                            print('expected')
                            expected_userLResult = test[USER_EXPECTED]
                            print(expected_userLResult)
                            expected_scoreLResult = test[SCORE_EXPECED]
                            print(expected_scoreLResult)
                            
                            self.assertEqual(len(actual_userLResult), len(expected_userLResult))
                            self.assertEqual(len(actual_scoresLResult), len(expected_scoreLResult))
                            self.assertEqual(actual_scoresLResult[0],expected_scoreLResult[0])
                            self.assertEqual(actual_scoresLResult[1],expected_scoreLResult[1])
                            self.assertEqual(actual_userLResult[0],expected_userLResult[0])
                            self.assertEqual(actual_userLResult[1],actual_userLResult[1])
                    
if __name__ == '__main__':
    unittest.main()