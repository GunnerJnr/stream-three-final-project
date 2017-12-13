"""
Tests.py: This file is responsible for running tests
to make sure that our app functions correctly.
"""
from unittest import TestCase


class SimpleTest(TestCase):
    """
    SimpleTest(TestCase): Create a class for our test functions
    """
    def test_adding_something_simple(self):
        """
        test_adding_something_simple(self):
        This simply tests adding two numbers and returning success
        on the test passing.
        """
        self.assertEqual(5 + 21, 26)

    def test_adding_something_not_equal(self):
        """
        test_adding_something_not_equal(self):
        This simply checks to numbers again but this time it checks if
        they are not equal.
        """
        self.assertNotEqual(11 + 29, 44)
