import unittest
from stack import Stack

class TestStack(unittest.TestCase):
  def test_create(self):
    stack = Stack()
    self.assertEqual(stack.isEmpty(), True)
