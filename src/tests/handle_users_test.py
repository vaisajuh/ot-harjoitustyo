import unittest
from handle_database import HandleDatabase

class TestHandleUsers(unittest.TestCase):
    def setUp(self):
        self.test = HandleDatabase()

    
    def test_empty_table(self):
        users = self.test.users.get_users()
        self.assertEqual(len(users), 0)
 
