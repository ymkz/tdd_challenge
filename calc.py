import math

class Calc:
  def __init__(self):
    self.tax = 1.1
  def calc_price(self, arr):
    return math.floor(sum(arr) * self.tax + 0.5)

if __name__ == '__main__':
  calc = Calc()
  print(calc.calc_price([10, 12]))
  print(calc.calc_price([40, 16]))
  print(calc.calc_price([100, 45]))
  print(calc.calc_price([50,50,55]))
  print(calc.calc_price([1000]))
  print(calc.calc_price([20, 40]))
  print(calc.calc_price([30, 60, 90]))
  print(calc.calc_price([11,12,13]))

# 24
# 62
# 160
# 171
# 1100
# 66
# 198
# 40
