# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:30:40 2019

@author: aleks
"""
import random
import warnings

class TrashBin:
    ''' Trash bin class '''
    ''' Two class variables all_coordinates and trash_counter store all coridantes of
    the trash bins and total number of created trashbins respectively '''
    all_coordinates = []
    trash_counter = 0
    random.seed(30)

    def __init__(self, map_origin, map_size, map_step):
        '''
        @param map_origin: single value of where does the map has its origin e.g. 0
        @type map_origin: int

        @param map_size: single value of where does the map has its end e.g. 100
        @type map_size: int

        @param map_step: single value of unit distance between nodes e.g. 10
        @type map_step: int
        '''
        '''
        Parametrized constructor of TrashBin class
        '''
        #Error handling
        if map_origin != 0:
            raise ValueError("Map must have its origin at 0")
        if map_step > map_size:
            raise ValueError("Step cannot be greater than map size")
        if map_size % map_step != 0:
            raise ValueError("Step must be a multple of map size")

        #after instance of the class is created we increse the class variable counter
        TrashBin.trash_counter += 1

        if TrashBin.trash_counter == 1:
            self.X_Y_coordinates = (random.randrange(map_origin + map_step, map_size, map_step),
                                    random.randrange(map_origin + map_step, map_size, map_step))
            TrashBin.all_coordinates.append(self.X_Y_coordinates)
        else: #here I try to aviod two bins having the same coordiantes, maybe can be done in a smarter way...
            self.X_Y_coordinates = (random.randrange(map_origin, map_size, map_step),
                                    random.randrange(map_origin, map_size, map_step))

            while self.X_Y_coordinates in TrashBin.all_coordinates or self.X_Y_coordinates == (0,0):
                self.X_Y_coordinates = (random.randrange(map_origin, map_size, map_step),
                                        random.randrange(map_origin, map_size, map_step))

            #coordinates are added to class variable all_coordinates in case we need it
            TrashBin.all_coordinates.append(self.X_Y_coordinates)

        self.filling_rate = random.randint(1, 10)
        self.current_level = random.randint(0, 50)
        self.capacity = 50
        self.bin_id = "bin#" + str(TrashBin.trash_counter)
        self.time_since_last_collection = 0

    def increment_trash(self):
        '''
        When this method is called, amount of trash is the bin is increased by the corresponding filling rate
        '''
        if self.current_level + self.filling_rate > self.capacity:
            warnings.warn("Exceeded trash limit, setting level to: %d" % (self.capacity))
            self.current_level = self.capacity
        else:
            self.current_level += self.filling_rate
        self.time_since_last_collection += 4.8



    def empty_trashbin(self):
        '''
        When this method is called, level of trash, for a given bin is set to 0
        '''
        self.current_level = 0
        self.time_since_last_collection = 0



if __name__ == '__main__':
    pass