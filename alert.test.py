import unittest
from infer_breach import infer_breach

class TestInferBreach(unittest.TestCase):
    
    def test_too_low(self):
        self.assertEqual(infer_breach(20, 50, 100), 'TOO_LOW')
        
    def test_too_high(self):
        self.assertEqual(infer_breach(110, 50, 100), 'TOO_HIGH')
        
    def test_normal(self):
        self.assertEqual(infer_breach(75, 50, 100), 'NORMAL')
        
    def test_at_lower_limit(self):
        self.assertEqual(infer_breach(50, 50, 100), 'NORMAL')
        
    def test_at_upper_limit(self):
        self.assertEqual(infer_breach(100, 50, 100), 'NORMAL')
        
    def test_below_lower_limit(self):
        self.assertEqual(infer_breach(49, 50, 100), 'TOO_LOW')
        
    def test_above_upper_limit(self):
        self.assertEqual(infer_breach(101, 50, 100), 'TOO_HIGH')
        
    def test_edge_case_lower(self):
     
        self.assertEqual(infer_breach(0, 0, 0), 'NORMAL')
        
    def test_edge_case_upper(self):
       
        self.assertEqual(infer_breach(0, 0, 0), 'NORMAL')
        
    def test_negative_temperature(self):
        self.assertEqual(infer_breach(-10, -20, -5), 'NORMAL')
        self.assertEqual(infer_breach(-30, -20, -5), 'TOO_LOW')
        self.assertEqual(infer_breach(0, -20, -5), 'TOO_HIGH')

if __name__ == '__main__':
    unittest.main()

