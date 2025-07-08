import unittest

from reverse import Reverse

class ReverseTests(unittest.TestCase):

    def test_no_characters(self):
        reverse = Reverse()
        string = ''
        actual = reverse.reverse(string);
        self.assertEqual(actual , '', 'Reverse one character failed')

    def test_one_character(self):
        reverse = Reverse()
        string = 'a'
        actual = reverse.reverse(string);
        self.assertEqual(actual , 'a', 'Reverse one character failed')

    def test_two_character(self):
        reverse = Reverse()
        string = 'az'
        actual = reverse.reverse(string);
        self.assertEqual(actual , 'za', 'Reverse two characters failed')

    def test_three_character(self):
        reverse = Reverse()
        string = 'ibm'
        actual = reverse.reverse(string);
        self.assertEqual(actual , 'mbi', 'Reverse two characters failed')

    def test_four_character(self):
        reverse = Reverse()
        string = 'fred'
        actual = reverse.reverse(string);
        self.assertEqual(actual , 'derf', 'Reverse two characters failed')

    def test_five_character(self):
        reverse = Reverse()
        string = 'fubar'
        actual = reverse.reverse(string);
        self.assertEqual(actual , 'rabuf', 'Reverse two characters failed')

if __name__ == '__main__':
    unittest.main()
