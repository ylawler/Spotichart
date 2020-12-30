import Project.UserInterface as ui

# -------------------------------------- TESTING ------------------------------------------
import unittest
from unittest import mock

class test_UserInterface(unittest.TestCase):

    def setup_UserInterface(self):
        self.ui = ui.UserInterface()

    def test_get_country_code(self):
        self.setup_UserInterface()

        # Values that should workd
        nl_inputs = ['The Netherlands', 'THE NETHERLANDS', 'the netherlands', 'netherlands', 'Netherlands', 'nl', 'NL']
        au_inputs = ['Australia','AUSTRALIA',  'australia', 'au']
        global_input = 'global'

        # Values that will fail
        input_fails = ['Stralia', '12345', 'Nethrelnds', 'blue']

        for nl_input in nl_inputs:
            self.assertEqual(self.ui.get_country_code(nl_input), 'nl')

        for au_input in au_inputs:
            self.assertEqual(self.ui.get_country_code(au_input), 'au')

        self.assertEqual(self.ui.get_country_code(global_input), 'global')

        for input_fail in input_fails:
            self.assertEqual(self.ui.get_country_code(input_fail), None)

    def test_invalid_country_code(self):
        self.setup_UserInterface()
        invalid_country = 'okdlakjda'
        self.assertIsNone(self.ui.get_country_code(invalid_country))

    def test_mock_user_input(self):
        self.setup_UserInterface()
        with mock.patch('builtins.input', side_effect = ['THe Netherlands', 'daily']):
            self.ui.get_user_input()
            self.assertEqual(self.ui.country_code, 'nl')
            self.assertEqual(self.ui.recurrence, 'daily')
            self.assertEqual(self.ui._num_retries, 0)

    def test_mock_input_aus(self):
        self.setup_UserInterface()
        with mock.patch('builtins.input', side_effect = ['Australia', 'weekly']):
            self.ui.get_user_input()
            self.assertEqual(self.ui.country_code, 'au')
            self.assertEqual(self.ui.recurrence, 'weekly')
            self.assertEqual(self.ui._num_retries, 0)

    def test_mock_input_us(self):
        self.setup_UserInterface()
        with mock.patch('builtins.input', side_effect = ['USA', 'daily']):
            self.ui.get_user_input()
            self.assertEqual(self.ui.country_code, 'us')
            self.assertEqual(self.ui.recurrence, 'daily')
            self.assertEqual(self.ui._num_retries, 0)

    def test_mock_input_false(self):
        self.setup_UserInterface()
        with mock.patch('builtins.input', side_effect = ['austral', 'Australia', 'd', 'daily']):
            self.ui.get_user_input()
            self.assertEqual(self.ui.country_code, 'au')
            self.assertEqual(self.ui.recurrence, 'daily')
            self.assertEqual(self.ui._num_retries, 2)


if __name__ == '__main__':
    unittest.main()
