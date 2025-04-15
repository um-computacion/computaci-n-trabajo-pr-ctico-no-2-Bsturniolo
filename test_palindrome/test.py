import unittest
from src.palindromes import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(is_palindrome("Neuquen"), True)
        self.assertEqual(is_palindrome("Radar"), True)
        self.assertEqual(is_palindrome("Ana"), True)

if __name__ == "__main__":
    unittest.main()