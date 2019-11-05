# -*- coding: utf-8 -*-
import warnings

class GarbageTruck:
	''' 
	Garbage Truck class 
	'''
	truckid = 0

	def __init__(self, origin, capacity):
		'''
		@param origin: tuple contiaing X and Y starting cordinates for the garbage truck
		@type origin: tuple
		'''
		'''
		Parametrized constructor of GarbageTruck class
		'''
		GarbageTruck.truckid += 1
		self.truckid = GarbageTruck.truckid
		self.origin = origin
		self.capacity = capacity #truck is able to collect 16 bins
		self.current_level = self.capacity
		self.time = 0
		self.bins_pickedup = 0
		self.distance = 0
		self.isfull = False

	def collect_trash(self, collected_amount):
		if self.current_level - collected_amount < 0:
			warnings.warn('Warning not all bins can be picked up !!!')
			self.isfull = True
			# raise ValueError("Garbage truck is full")
		else:
			self.current_level -= collected_amount
			self.bins_pickedup += 1

	def update_data(self, distance, step):
		self.distance = distance
		self.time = (self.bins_pickedup * 10) + (distance / step * 15)

	def empty_truck(self):
		'''
		When this method is called, level of trash, for a given bin is set to 0
		'''
		self.current_level = self.capacity
		self.time = 0
		self.distance = 0
		self.isfull = False

	def print_data(self):
		print("Truck id: %d, distance travelled: %d, total time in minutes: %d" % (self.truckid, self.distance, self.time))
		
if __name__ == '__main__':
    pass
