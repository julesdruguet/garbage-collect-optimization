# -*- coding: utf-8 -*-

class GarbageTruck:
    ''' Garbage Truck class '''


    def __init__(self, origin):
		'''
		@param origin: tuple contiaing X and Y starting cordinates for the garbage truck
		@type origin: tuple
		'''
		'''
		Parametrized constructor of GarbageTruck class
		'''
		self.origin = origin
		self.capacity = 50 * 16 #truck is able to collect 16 bins
		self.current_level = self.capacity

	def collect_trash(self, collected_amount):
		if self.current_level - collected_amount < 0:
			raise ValueError("Garbage truck is full")
		self.current_level = self.capacity - collected_amount

	def empty_trashbin(self):
		'''
		When this method is called, level of trash, for a given bin is set to 0
		'''
		self.current_level = 0
		
if __name__ == '__main__':
    pass
