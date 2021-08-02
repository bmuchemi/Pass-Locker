import unittest
from users import User

class UserTest(unittest.TestCase):

    def setUp(self):
       self.new_user=User("Benjamin","pass")

    def test_init(self):
        self.assertEqual(self.new_user.init_username,"James")
        self.assertEqual(self.new_user.init_password,"1234")

if __name__ == '__main__':
    unittest.main()