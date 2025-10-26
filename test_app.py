import unittest
from app import greet_user, add_numbers, reverse_string

class TestApp(unittest.TestCase):
    def test_greet_user_with_name(self):
        self.assertEqual(greet_user("Alice"), "Hello, Alice!")
    
    def test_add_numbers_positive(self):
        self.assertEqual(add_numbers(5, 3), 8)
    
    def test_reverse_string_simple(self):
        self.assertEqual(reverse_string("hello"), "olleh")

if __name__ == "__main__":
    unittest.main()
