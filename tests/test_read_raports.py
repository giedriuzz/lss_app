import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import unittest
from unittest.mock import patch
from read_raports import get_raport_description_from_raport_dictionary

class TestGetRaportDescriptionFromRaportDictionary(unittest.TestCase):
    def setUp(self):
        # Mock dictionary structure
        self.mock_dictionary = [
            {
                "radio_raports": {
                    "test_raport": {
                        "description": "This is a test description",
                        "keys": {}
                    }
                }
            }
        ]

    @patch("builtins.print")
    def test_valid_dictionary_key_and_value(self, mock_print):
        get_raport_description_from_raport_dictionary(
            dictionary=self.mock_dictionary,
            dictionary_key="radio_raports",
            value_name="test_raport"
        )
        mock_print.assert_called_once_with("This is a test description")

    @patch("builtins.print")
    def test_missing_description(self, mock_print):
        self.mock_dictionary[0]["radio_raports"]["test_raport"]["description"] = None
        get_raport_description_from_raport_dictionary(
            dictionary=self.mock_dictionary,
            dictionary_key="radio_raports",
            value_name="test_raport"
        )
        mock_print.assert_called_once_with("")

    def test_invalid_dictionary_key(self):
        with self.assertRaises(KeyError):
            get_raport_description_from_raport_dictionary(
                dictionary=self.mock_dictionary,
                dictionary_key="invalid_key",
                value_name="test_raport"
            )

    def test_invalid_value_name(self):
        with self.assertRaises(KeyError):
            get_raport_description_from_raport_dictionary(
                dictionary=self.mock_dictionary,
                dictionary_key="radio_raports",
                value_name="invalid_value"
            )

if __name__ == "__main__":
    unittest.main()
