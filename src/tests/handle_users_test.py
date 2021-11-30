import unittest
from handle_database import HandleDatabase


class TestHandleUsers(unittest.TestCase):
    def setUp(self):
        self.test = HandleDatabase()
        self.test.clear_database()


    def test_insert_user(self):
        self.test.users.insert_user("Michelin", "1234")
        get = self.test.users.get_users()
        value = get[0]
        self.assertEqual(value, "michelin, 1234")


    def test_validate_password(self):
        user_creation = self.test.users.validate_password("Michelin", "1234")
        self.assertEqual(user_creation, 1)
        invalid_pass = self.test.users.validate_password("Michelin", "1235")
        self.assertEqual(invalid_pass, False)
        correct_pass = self.test.users.validate_password("Michelin", "1234")
        self.assertEqual(correct_pass, 1)
