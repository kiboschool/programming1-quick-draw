from unittest.mock import patch
from unittest import TestCase
import unittest
import sys


class Test(TestCase):
    @patch('builtins.input', side_effect=["1", "21"])
    @patch('time.time', side_effect=[0., 0.09])
    # def test_enough_for_one(self, mock_time, mock_input, mock_print):
    def test_drew_too_soon(self, mock_time, mock_input):
        with patch('builtins.print') as mock_print:
            import main
        sys.modules.pop('main')
        expected_printouts = [
         'DRAW!',
         'You took 0.09 seconds',
         "You pressed Enter too soon, didn't you?"]
        print(mock_print.call_args_list[-1])
        used_args = [call[0][0] if len(call[0]) else '' for call in mock_print.call_args_list]
        self.assertEqual(used_args[-3:], expected_printouts)

    @patch('builtins.input', side_effect=["1", "21"])
    @patch('time.time', side_effect=[0., 0.2778])
    def test_fastest_draw(self, mock_time, mock_input):
        with patch('builtins.print') as mock_print:
            import main
        sys.modules.pop('main')
        expected_printouts = [
         'DRAW!',
         'You took 0.2778 seconds',
         "You're the fastest draw in the west, congratulations!"]
        print(mock_print.call_args_list[-1])
        used_args = [call[0][0] if len(call[0]) else '' for call in mock_print.call_args_list]
        self.assertEqual(used_args[-3:], expected_printouts)

    @patch('builtins.input', side_effect=["1", "21"])
    @patch('time.time', side_effect=[0., 0.316])
    def test_slow_draw(self, mock_time, mock_input):
        with patch('builtins.print') as mock_print:
            import main
        sys.modules.pop('main')
        expected_printouts = [
         'DRAW!',
         'You took 0.316 seconds',
         "Too slow! Try again next time."]
        print(mock_print.call_args_list[-1])
        used_args = [call[0][0] if len(call[0]) else '' for call in mock_print.call_args_list]
        self.assertEqual(used_args[-3:], expected_printouts)

if __name__ == '__main__':
    unittest.main()
