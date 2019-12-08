# -*- coding: utf-8 -*-
import warnings

class GarbageTruck:
	''' 
	Garbage Truck class 
	'''
	truckid = 0

	def __init__(self, origin, capacity, step):
		'''
		@param origin: tuple contiaing X and Y starting cordinates for the garbage truck
		@type origin: tuple
		'''
		'''
		Parametrized constructor of GarbageTruck class
		'''
		GarbageTruck.truckid += 1
		self.truckid = "truck#" + str(GarbageTruck.truckid)
		self.origin = origin
		self.capacity = capacity #truck is able to collect 16 bins
		self.space_left = self.capacity
		self.time = 0
		self.bins_pickedup = 0
		self.distance = 0
		self.isfull = False
		self.map_step = step

	def collect_trash(self, collected_amount):
		if self.space_left - collected_amount < 0:
			warnings.warn('Warning not all bins can be picked up !!!')
			self.isfull = True
			# raise ValueError("Garbage truck is full")
		else:
			self.space_left -= collected_amount
			self.bins_pickedup += 1

	def update_truck_data(self, distance):
		self.distance = distance
		self.time = (self.bins_pickedup * 2) + (distance / self.map_step * 7)
		self.trash_collected = self.capacity - self.space_left

	def empty_truck(self):
		'''
		When this method is called, level of trash, for a given bin is set to 0
		'''
		self.space_left = self.capacity
		self.time = 0
		self.distance = 0
		self.isfull = False

	def get_truck_data(self, i):
		print("Truck id: %s, distance travelled: %d, total time in minutes: %d, total trash picked up: %d" % 
			(self.truckid, self.distance, self.time, self.trash_collected))
		return [i, self.truckid, self.distance, self.time, self.trash_collected]
		
if __name__ == '__main__':
    pass
