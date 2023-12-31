import unittest
import main

class TestMain(unittest.TestCase):
    def test_get_word_count(self):
        self.assertEqual(main.get_word_count("This should be 4"), 4, "Should be 4")
        self.assertEqual(main.get_word_count(""), 0, "Should be 0")
    
    def test_get_character_count(self):
        expected_char_dict = {
            ' ': 3,
            '@': 1,
            'a': 3,
            'b': 2,
            'c': 2,
        }
        self.assertDictEqual(main.get_character_count("Aaa Bb Cc @"), expected_char_dict)
        self.assertDictEqual(main.get_character_count(""), {})

    def test_format_report(self):
        self.maxDiff = None
        document = "Hello world, test document report"

        report = """--- Begin report of books/frankenstein.txt ---
5 words found in the document

The 'e' character was found 4 times
The 'o' character was found 4 times
The 't' character was found 4 times
The 'l' character was found 3 times
The 'r' character was found 3 times
The 'd' character was found 2 times
The 'h' character was found 1 times
The 'w' character was found 1 times
The 's' character was found 1 times
The 'c' character was found 1 times
The 'u' character was found 1 times
The 'm' character was found 1 times
The 'n' character was found 1 times
The 'p' character was found 1 times
--- End report ---"""

        self.assertEqual(main.format_report("books/frankenstein.txt", 5, main.get_character_count(document)), report)

if __name__ == "__main__":
    unittest.main()
