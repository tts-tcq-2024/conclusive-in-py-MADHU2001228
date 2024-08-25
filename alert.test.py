import unittest
from classify_temperature_breach import classify_temperature_breach
from infer_breach import infer_breach
from check_and_alert import check_and_alert
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')


if __name__ == '__main__':
  unittest.main()
