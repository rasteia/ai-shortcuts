import unittest
import doctest
import pytest
import nose

## testScript.py - Automated Testing Scripts: List python scripts that run unit tests or integration tests 
  # can be very helpful in maintaining the quality of the code.

# ----- Unit Tests using unittest -----

class MyUnitTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
    
    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

# ----- Pytest Tests -----

def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 5 - 3 == 2

# ----- Doctest -----

def add(x, y):
    """
    Add two numbers.

    >>> add(2, 2)
    4
    >>> add(5, 3)
    8
    """
    return x + y

# ----- Nose Tests -----

def test_multiplication():
    assert 2 * 3 == 6

# ----- Main Script -----

if __name__ == '__main__':
    # Run unittest
    unittest.main(argv=['ignored'], exit=False)
    
    # Run pytest
    pytest.main(['-s'])
    
    # Run doctest
    doctest.testmod()
    
    # Run nose
    nose.run(argv=['ignored'])
