import unittest
from database.handle_database import HandleDatabase


class TestHandleContacts(unittest.TestCase):
    def setUp(self):
        self.test = HandleDatabase()
        self.test._clear_database()
        self.test.users.insert_user("Michelin", "1234")
        self.test.contacts.insert_contact(
            1, "testi", "katu", "a@a.com", "12345")

    def test_insert_contact(self):
        contact = self.test.contacts.get_contacts(1, '', '', '', '')
        self.assertEqual(contact[0], ('testi', 'katu', 'a@a.com', '12345', 1))

    def test_delete_contact(self):
        self.test.contacts.delete_contact(1)
        contact = self.test.contacts.get_contacts(1, '', '', '', '')
        self.assertEqual(len(contact), 0)
    
    def test_get_row(self):
        get_row = self.test.contacts.get_row(1)
        self.assertEqual(get_row[0], "testi")
        self.assertEqual(get_row[1], "katu")
        self.assertEqual(get_row[2], "a@a.com")
        self.assertEqual(get_row[3], "12345")
    

    def test_update_row(self):
        self.test.contacts.update_row(1, 'jees-mies', 'kuja', 'x@x.fi', 55555)
        get_row = self.test.contacts.get_row(1)
        self.assertEqual(get_row[0], "jees-mies")
        self.assertEqual(get_row[1], "kuja")
        self.assertEqual(get_row[2], "x@x.fi")
        self.assertEqual(get_row[3], "55555")