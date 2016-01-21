import unittest
# import sys
# from io import StringIO
from unittest.mock import patch


def get_number():
    """Return an integer that the user enters."""
    while True:
        choice = input("please enter an integer (will be truncated if it is a float): ")
        try:
            num = int(choice)
            break
        except ValueError:
            continue
    return num


class StdinPatchTest(unittest.TestCase):

    @patch('builtins.input', return_value='45')
    def test_get_number(self):
        self.assertEqual(get_number(), 45)
