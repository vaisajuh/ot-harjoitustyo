import unittest
from database.handle_database import HandleDatabase


class TestHandleUsers(unittest.TestCase):
    def setUp(self):
        self.test = HandleDatabase()
        self.test.clear_database()
        self.user = self.test.users._insert_user("Michelin", "1234")

    def test_insert_user(self):
        get_user = self.test.users._get_user("michelin")
        name = get_user[1]
        password = get_user[2]
        self.assertEqual(name, "michelin")
        self.assertEqual(password, "1234")

    def test_validate_password(self):
        invalid_pass = self.test.users.validate_password("Michelin", "1235")
        self.assertEqual(invalid_pass, False)
        correct_pass = self.test.users.validate_password("Michelin", "1234")
        self.assertEqual(correct_pass, 1)

    def test_validate_count_0(self):
        user_creation = self.test.users.validate_password("Monica", "1234")
        self.assertEqual(user_creation, 2)
