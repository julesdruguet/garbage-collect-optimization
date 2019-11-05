import sys
sys.path.insert(1, '../')
import unittest
from trashbin import TrashBin

class TestTrashBin(unittest.TestCase):
	def test_origin(self):
		self.assertRaises(ValueError, TrashBin, 1, 100, 10)
	def test_step_bigger(self):
		self.assertRaises(ValueError, TrashBin, 0, 1, 10)
	def test_step_not_multiple(self):
		self.assertRaises(ValueError, TrashBin, 0, 100, 7)	
    
if __name__ == '__main__':
    unittest.main()