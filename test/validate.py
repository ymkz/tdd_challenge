import sys
import unittest
from validate import Validate
from io import StringIO

class TestValidate(unittest.TestCase):
  def test_validate_addr_spec(self):
    cases = 'abc@example.com\na..bc@example.com\n'
    dummy_in = StringIO(cases)
    dummy_out = StringIO()
    # 実際に実行する
    validate = Validate()
    validate.validate_addr_spec(dummy_in, dummy_out)
    # 結果の比較
    result = dummy_out.getvalue()
    self.assertEqual(result, 'ok\nng\n')
