import unittest
from unittest.mock import patch
from io import StringIO
import dictionary_tool


class TestDictionaryTool(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_lookup_word_successful(self, mock_stdout):
        dictionary_tool.DictionaryTool.API_KEY = 'YOUR_MOCK_API_KEY'

        tool = dictionary_tool.DictionaryTool()
        tool.lookup_word('example')

        expected_output = '''Pronunciation: ig-ˈzam-pəl
Short Definitions:
1. a representative part or a single item from a larger whole or group especially when presented for inspection or shown as evidence of quality : specimen
2. a typical or representative example'''
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_lookup_word_no_results(self, mock_stdout):
        dictionary_tool.DictionaryTool.API_KEY = 'YOUR_MOCK_API_KEY'

        tool = dictionary_tool.DictionaryTool()
        tool.lookup_word('nonexistent')

        expected_output = 'No results found for the word: nonexistent'
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()

