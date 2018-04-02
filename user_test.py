import unittest
from  user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Mary","Anne","mary@gmail.com",)
    def test1(self):
        self.assertEqual(self.new_user.f_name,"Mary")
        self.assertEqual(self.new_user.m_name,"Anne")
        self.assertEqual(self.new_user.e_mail,"mary@gmail.com")
    def test_save_user(self):
        self.new_user.save_user()
 
    def tearDown(self):
        User.userlist = []
    def test_delete_user(self):
        self.new_user.save_user()
        test_data= User("fina","gathoni","fina@gmail.com")
        test_data.save_user()
        self.assertEqual(len(User.user_list),2)
if __name__ == '__main__':
    unittest.main()