import unittest
from users import User
from users import Credentials

class UserTest(unittest.TestCase):
    def setUp(self):
        """
        method run before each test
        """
        self.new_account = Credentials("twitter","Benjamin","1234")
        

    def test_init(self):

         self.assertEqual(self.new_account("twitter","Benjamin","12345t"))

    
    def tearDown(self):
        '''
        method called after each user test
        '''
        User.users_list= []