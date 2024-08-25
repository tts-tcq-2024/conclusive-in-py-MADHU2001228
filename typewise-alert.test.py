import unittest
from breach_classify import infer_breach

class TestInferBreach(unittest.TestCase):
    
    def test_too_low(self):
        # Value below the lower limit
        self.assertEqual(infer_breach(20, 50, 100), 'TOO_LOW')
    
    def test_too_high(self):
        # Value above the upper limit
        self.assertEqual(infer_breach(110, 50, 100), 'TOO_HIGH')
    
    def test_normal(self):
        # Value within the limits
        self.assertEqual(infer_breach(75, 50, 100), 'NORMAL')
    
    def test_at_lower_limit(self):
        # Value exactly at the lower limit
        self.assertEqual(infer_breach(50, 50, 100), 'NORMAL')
    
    def test_at_upper_limit(self):
        # Value exactly at the upper limit
        self.assertEqual(infer_breach(100, 50, 100), 'NORMAL')
    
    def test_below_lower_limit(self):
        # Value just below the lower limit
        self.assertEqual(infer_breach(49, 50, 100), 'TOO_LOW')
    
    def test_above_upper_limit(self):
        # Value just above the upper limit
        self.assertEqual(infer_breach(101, 50, 100), 'TOO_HIGH')
    
    def test_edge_case_lower(self):
        # Testing with lower limit value exactly at the boundary
        self.assertEqual(infer_breach(0, 0, 0), 'NORMAL')
    
    def test_edge_case_upper(self):
        # Testing with upper limit value exactly at the boundary
        self.assertEqual(infer_breach(0, 0, 0), 'NORMAL')
    
    def test_negative_temperature(self):
        # Negative temperatures within, below, and above limits
        self.assertEqual(infer_breach(-10, -20, -5), 'NORMAL')
        self.assertEqual(infer_breach(-30, -20, -5), 'TOO_LOW')
        self.assertEqual(infer_breach(0, -20, -5), 'TOO_HIGH')
    
    def test_zero_limits(self):
        # Edge case where limits are zero
        self.assertEqual(infer_breach(0, 0, 0), 'NORMAL')
        self.assertEqual(infer_breach(-1, 0, 0), 'TOO_LOW')
        self.assertEqual(infer_breach(1, 0, 0), 'TOO_HIGH')
    
    def test_large_values(self):
        # Test with very large values
        self.assertEqual(infer_breach(1e6, 0, 1e6), 'NORMAL')
        self.assertEqual(infer_breach(-1e6, 0, 1e6), 'TOO_LOW')
        self.assertEqual(infer_breach(2e6, 0, 1e6), 'TOO_HIGH')

if __name__ == '__main__':
    unittest.main()
