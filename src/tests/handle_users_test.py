import unittest
from handle_database import HandleDatabase

class TestHandleUsers(unittest.TestCase):
    def setUp(self):
        self.test = HandleDatabase()
        self.test.clear_database()
    
    
    def test_empty_table(self):
        users = self.test.users.get_users()
        self.assertEqual(len(users), 0)
    
    
    def test_insert_user(self):
        self.test.users.insert_user("Michelin", "1234")
        get = self.test.users.get_users()
        value = get[0]
        self.assertEqual(value, "Michelin, 1234")

 
 