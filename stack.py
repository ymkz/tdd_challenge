class Stack:
  def __init__(self, val=[]):
    self.value = val
  def isEmpty(self):
    return len(self.value) == 0
  def size(self):
    return len(self.value)
