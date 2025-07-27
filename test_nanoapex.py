# test_nanoapex.py
"""
Tests for NanoApex module.
"""

import unittest
from nanoapex import NanoApex

class TestNanoApex(unittest.TestCase):
    """Test cases for NanoApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NanoApex()
        self.assertIsInstance(instance, NanoApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NanoApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
