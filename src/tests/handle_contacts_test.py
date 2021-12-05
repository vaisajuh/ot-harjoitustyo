import unittest
from handle_database import HandleDatabase


class TestHandleContacts(unittest.TestCase):
    def setUp(self):
        self.test = HandleDatabase()
        self.test.clear_database()
        self.test.users.insert_user("Michelin", "1234")
        self.test.contacts.insert_contact(
            1, "testi", "katu", "a@a.com", "12345")


    def test_insert_contact(self):
        contact = self.test.contacts.get_contacts(1)
        self.assertEqual(contact[0], ('testi', 'katu', 'a@a.com', '12345', 1))
    
    def test_delete_contact(self):
        self.test.contacts.delete_contact(1)
        contact = self.test.contacts.get_contacts(1)
        self.assertEqual(len(contact), 0)