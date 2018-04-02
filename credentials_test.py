import unittest
from credentials import Info

class TestInfo(unittest.TestCase):
    def setUp(self):
        self.new_info =Info("mary.anne","anne.mary")
    def test_init(self):
        self.assertEqual(self.new_info.face_bookp,"mary.anne")
        self.assertEqual(self.new_info.email_p,"anne.mary")
if __name__ == '__main__':
    unittest.main()
