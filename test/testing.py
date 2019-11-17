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
	def test_bins_inside_map(self):
		map_origin = 0
		map_size = 1000
		map_step = 100
		#initial parameters of simulation
		amount_of_trash_bins = 10
		bins = [TrashBin(map_origin, map_size, map_step) for x in range(amount_of_trash_bins)]
		for x in bins:
			self.assertTrue(x.X_Y_coordinates <= (map_size, map_size))
    
if __name__ == '__main__':
    unittest.main()