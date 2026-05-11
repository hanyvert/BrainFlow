# test_brainflow.py
"""
Tests for BrainFlow module.
"""

import unittest
from brainflow import BrainFlow

class TestBrainFlow(unittest.TestCase):
    """Test cases for BrainFlow class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BrainFlow()
        self.assertIsInstance(instance, BrainFlow)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BrainFlow()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
