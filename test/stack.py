import unittest
from stack import Stack

class TestStack(unittest.TestCase):
  def test_create(self):
    stack = Stack()
    self.assertEqual(stack.isEmpty(), True)

  def test_size(self):
    stack = Stack()
    self.assertEqual(stack.size(), 0)
    stack = Stack([1,2])
    self.assertEqual(stack.size(), 2)
