import unittest
from calc import Calc
from io import StringIO
import sys

class TestCalc(unittest.TestCase):
  def test_calc_price(self):
    calc = Calc()
    self.assertEqual(calc.calc_price([]), 0)
    self.assertEqual(calc.calc_price([10, 12]), 24)
    self.assertEqual(calc.calc_price([40, 16]), 62)
    self.assertEqual(calc.calc_price([100, 45]), 160)
    self.assertEqual(calc.calc_price([50, 50, 55]), 171)

  def test_input_calc(self):
    # IOをいじる
    dummy_in = StringIO("""10,12
40,16
100,45

50,50,55


""")

    dummy_out = StringIO()
    # 実際に実行する
    calc = Calc()
    calc.input_calc(dummy_in, dummy_out)
    # 結果の比較
    result = dummy_out.getvalue()
    self.assertEqual(result, """24
62
160
0
171
""")
