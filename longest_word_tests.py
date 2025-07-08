import unittest

from longest_word import LongestWord

class LongestWordTests(unittest.TestCase):

    def test_long_sentence_1(self):
        longest_word = LongestWord('a tiny sentence that has words of various sizes')
        word = longest_word.longest_word();
        length = longest_word.length_of_longest_word();
        self.assertEqual(word , 'sentence', 'Is not the longest word')
        self.assertEqual(length , 8, 'Is not the length of the longest work')

    def test_long_sentence_2(self):
        longest_word = LongestWord('the quick brown fox jumps over the lazy dog')
        word = longest_word.longest_word();
        length = longest_word.length_of_longest_word();
        self.assertEqual(word , 'quick', 'Is not the longest word')
        self.assertEqual(length , 5, 'Is not the length of the longest work')

if __name__ == '__main__':
    unittest.main()
