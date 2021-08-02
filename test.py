import unittest
from users import User
from users import Credentials

class LockerTest(unittest.TestCase):
    def setUp(self):
        """
        method run before each test
        """
        self.new_account = Credentials("instagram","linda","myPassword")
    
    def tearDown(self):
        '''
        method called after each user test
        '''
        User.data_user = []