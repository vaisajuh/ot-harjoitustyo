import unittest
from database.handle_database import HandleDatabase



class TestHandleUsers(unittest.TestCase):
    def setUp(self):
        self.test = HandleDatabase()
        self.test._clear_database()
        self.user = self.test.users.insert_user("Michelin", "1234")

    def test_insert_user(self):
        get_user = self.test.users._get_user("michelin")
        add_user = self.test.users.insert_user("michelin", "1234")
        name = get_user[1]
        password = get_user[2]
        hash = self.test.users._create_hash("1234")
        self.assertEqual(name, "michelin")
        self.assertEqual(password, hash)
        self.assertEqual(add_user, False)

    def test_validate_password(self):
        new_user = self.test.users.validate_password("kate", "1234")
        invalid_pass = self.test.users.validate_password("Michelin", "1235")
        correct_pass = self.test.users.validate_password("Michelin", "1234")
        self.assertEqual(invalid_pass, False)
        self.assertEqual(correct_pass, 1)
        self.assertEqual(new_user, False)
    
    def test_validate_length(self):
        invalid_length = self.test.users.validate_length("ab", "abcd")
        valid_length = self.test.users.validate_length("abc", "abcde")
        self.assertEqual(invalid_length, False)
        self.assertEqual(valid_length, True)
