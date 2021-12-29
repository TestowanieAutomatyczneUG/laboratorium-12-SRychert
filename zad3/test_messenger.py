from unittest import TestCase
from unittest.mock import *
from messenger import Messenger


class TestMessenger(TestCase):
    def setUp(self):
        self.temp = Messenger()

    @patch.object(Messenger, "send_msg")
    def test_send_msg(self, mock_send_msg):
        mock_send_msg.return_value = 'Message send'
        self.assertEqual(self.temp.send_msg('client@example.com', 'Content'), 'Message send')

    @patch.object(Messenger, "send_msg")
    def test_send_msg_wrong_type_client(self, mock_send_msg):
        mock_send_msg.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.send_msg, None, 'Content')

    @patch.object(Messenger, "send_msg")
    def test_send_msg_wrong_type_client(self, mock_send_msg):
        mock_send_msg.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.send_msg, 'client@example.com', None)

    @patch.object(Messenger, "send_msg")
    def test_send_msg_wrong_type_both(self, mock_send_msg):
        mock_send_msg.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.send_msg, None, None)

    @patch.object(Messenger, "receive_msg")
    def test_receive_msg(self, mock_receive_msg):
        mock_receive_msg.return_value = ['Msg One', 'Msg Two']
        self.assertEqual(self.temp.receive_msg('example@example.com'), ['Msg One', 'Msg Two'])

    @patch.object(Messenger, "receive_msg")
    def test_receive_msg_empty(self, mock_receive_msg):
        mock_receive_msg.return_value = []
        self.assertEqual(self.temp.receive_msg('example@example.com'), [])

    @patch.object(Messenger, "receive_msg")
    def test_receive_msg_wrong_type(self, mock_receive_msg):
        mock_receive_msg.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.receive_msg, None)

    def tearDown(self):
        self.temp = None
