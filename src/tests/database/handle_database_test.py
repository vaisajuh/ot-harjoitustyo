import unittest
from database.handle_database import HandleDatabase

class TestHandleDatabase(unittest.TestCase):

    def setUp(self):
        self.test = HandleDatabase()
        self.test._clear_database()
        
    
    def test_initialize_database(self):
        count_tables = self.test.database.execute('SELECT COUNT(*) FROM sqlite_master WHERE type="table"').fetchone()[0]
        self.assertEqual(count_tables, 2)
    
    def test_clear_database(self):
        count_users = self.test.database.execute('SELECT COUNT(*) FROM Users').fetchone()[0]
        count_contacts = self.test.database.execute('SELECT COUNT(*) FROM Contacts').fetchone()[0]
        self.assertEqual(count_users, 0)
        self.assertEqual(count_contacts, 0)