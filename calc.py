import sys
import math

class Calc:
  def __init__(self):
    self.tax = 1.1
  def calc_price(self, arr):
    return math.floor(sum(arr) * self.tax + 0.5)

  def input_calc(self, in_stream, out_stream):
    results = []
    for line in in_stream.readlines():
        price_list = []
        if line != "\n":
            price_list = [int(n) for n in line.replace('\n','').split(',')]
        results.append(self.calc_price(price_list))
    for i in range(len(results)-1):
        out_stream.write(str(results[i]) + "\n")

if __name__ == '__main__':
  calc = Calc()
  calc.input_calc(sys.stdin, sys.stdout)
