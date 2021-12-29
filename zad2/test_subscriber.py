from unittest import TestCase, main
from unittest.mock import *
from subscriber import Subscriber


class SubscriberTest(TestCase):
    def setUp(self) -> None:
        self.temp = Subscriber()

    @patch.object(Subscriber, 'add_client')
    def test_add_client_to_empty_list(self, mock_add_client):
        mock_add_client.return_value = ["Maciek"]
        self.assertEqual(self.temp.add_client("Maciek"), ["Maciek"])

    @patch.object(Subscriber, 'add_client')
    def test_add_client_wrong_type(self, mock_add_client):
        mock_add_client.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add_client, ["Jacek"])

    @patch.object(Subscriber, 'add_client')
    def test_add_client_again(self, mock_add_client):
        mock_add_client.side_effect = [["Maciek"], ValueError]
        self.temp.add_client("Maciek")
        self.assertRaises(ValueError, self.temp.add_client, "Maciek")

    @patch.object(Subscriber, 'delete_client')
    def test_delete_client_empty_list(self, mock_delete_client):
        mock_delete_client.side_effect = ValueError
        self.assertRaises(ValueError, self.temp.delete_client, "Jacek")

    @patch.object(Subscriber, 'delete_client')
    def test_delete_client_one(self, mock_delete_client):
        mock_delete_client.return_value = []
        self.assertEqual(self.temp.delete_client("Jacek"), [])

    @patch.object(Subscriber, 'delete_client')
    def test_delete_client_not_empty(self, mock_delete_client):
        mock_delete_client.return_value = ["Jacek"]
        self.assertEqual(self.temp.delete_client("Maciek"), ["Jacek"])

    @patch.object(Subscriber, 'delete_client')
    def test_delete_client_wrong_type(self, mock_delete_client):
        mock_delete_client.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.delete_client, ["Jacek"])

    @patch.object(Subscriber, 'msg_client')
    def test_msg_client_empty(self, mock_msg_client):
        mock_msg_client.side_effect = ValueError
        self.assertRaises(ValueError, self.temp.msg_client, "Jacek", "hey")

    @patch.object(Subscriber, 'msg_client')
    def test_msg_client_wrong_type(self, mock_msg_client):
        mock_msg_client.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.msg_client, ["Jacek", "hey"])

    @patch.object(Subscriber, 'msg_client')
    def test_msg_client(self, mock_msg_client):
        mock_msg_client.return_value = True
        self.assertTrue(self.temp.msg_client("Maciek", "hello"))

    def tearDown(self) -> None:
        self.temp = None
