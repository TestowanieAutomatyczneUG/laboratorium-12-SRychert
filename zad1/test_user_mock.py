from unittest import TestCase, mock
from user import User
import json


def load_mock_data():
    with open("data.txt", "r") as f:
        return json.loads(f.read())


class TestUser(TestCase):
    def setUp(self) -> None:
        self.patcher = mock.patch('user.User.get_data', return_value=load_mock_data())
        self.patcher.start()
        self.temp = User()

    def test_get_email(self):
        self.assertEqual(self.temp.get_email(), "salman.nesvik@example.com")

    def test_get_full_name(self):
        self.assertEqual(self.temp.get_full_name(), "Mr Salman Nesvik")

    def test_is_living_on_northern_hemisphere(self):
        self.assertTrue(self.temp.is_living_on_northern_hemisphere())

    def tearDown(self) -> None:
        self.patcher.stop()
        self.temp = None
