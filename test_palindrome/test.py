import unittest
from src.palindromes import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(is_palindrome("Neuquen"), True)
        self.assertEqual(is_palindrome("Radar"), True)
        self.assertEqual(is_palindrome("Ana"), True)
        
    def test_palindrome2(self):
        self.assertEqual(is_palindrome("Eve"), True)
        self.assertEqual(is_palindrome("Reviver"), True)
        self.assertEqual(is_palindrome("Ojo rojo"), True)
        
    def test_palindrome3(self):
        self.assertEqual(is_palindrome("Ala"), True)
        self.assertEqual(is_palindrome("Oso"), True)
        self.assertEqual(is_palindrome("Ama"), True)
    
class TestPalindromesEdgeCases(unittest.TestCase):

    def test_cadena_vacia(self):
        self.assertTrue(is_palindrome(""))
    def test_una_letra_minuscula(self):
        self.assertTrue(is_palindrome("s"))
    def test_una_letra_mayuscula(self):
        self.assertTrue(is_palindrome("L"))

if __name__ == "__main__":
    unittest.main() 