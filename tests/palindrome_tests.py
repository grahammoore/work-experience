import unittest

from src.palindrome import Palindrome

class PalindromeTests(unittest.TestCase):

    def test_no_characters(self):
        palindrome = Palindrome()
        string = ''
        actual = palindrome.is_a_palindrome(string);
        self.assertFalse(actual , 'Is not a palindrom')

    def test_one_character(self):
        palindrome = Palindrome()
        string = 'a'
        actual = palindrome.is_a_palindrome(string);
        self.assertTrue(actual , 'Is not a palindrom')

    def test_two_characters_is_a_palindrome(self):
        palindrome = Palindrome()
        string = 'aa'
        actual = palindrome.is_a_palindrome(string);
        self.assertTrue(actual , 'Is not a palindrome')

    def test_two_characters_is_not_a_palindrome(self):
        palindrome = Palindrome()
        string = 'az'
        actual = palindrome.is_a_palindrome(string);
        self.assertFalse(actual , 'Is a palindrome')

    def test_three_characters_is_a_palindrome(self):
        palindrome = Palindrome()
        string = 'lol'
        actual = palindrome.is_a_palindrome(string);
        self.assertTrue(actual , 'Is not a palindrome')

    def test_three_characters_is_not_a_palindrome(self):
        palindrome = Palindrome()
        string = 'ibm'
        actual = palindrome.is_a_palindrome(string);
        self.assertFalse(actual , 'Is a palindrome')

    def test_four_characters_is_a_palindrome(self):
        palindrome = Palindrome()
        string = 'beeb'
        actual = palindrome.is_a_palindrome(string);
        self.assertTrue(actual , 'Is not a palindrome')

    def test_four_characters_is_not_a_palindrome(self):
        palindrome = Palindrome()
        string = 'rock'
        actual = palindrome.is_a_palindrome(string);
        self.assertFalse(actual , 'Is a palindrome')

    def test_five_characters_is_a_palindrome(self):
        palindrome = Palindrome()
        string = 'radar'
        actual = palindrome.is_a_palindrome(string);
        self.assertTrue(actual , 'Is not a palindrome')

    def test_five_characters_is_not_a_palindrome(self):
        palindrome = Palindrome()
        string = 'tacos'
        actual = palindrome.is_a_palindrome(string);
        self.assertFalse(actual , 'Is a palindrome')

if __name__ == '__main__':
    unittest.main()
