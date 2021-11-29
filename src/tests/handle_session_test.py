import unittest
from session.handle_session import HandleSession

class TestHandleSession(unittest.TestCase):
    def setUp(self):
        self.test = HandleSession()
    

    def test_session(self):
        self.test.add_session(1)
        get_id = self.test.get_session()
        self.assertEqual(get_id, 1)