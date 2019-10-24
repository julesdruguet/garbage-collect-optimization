# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:30:40 2019

@author: aleks
"""
import random

class TrashBin:
    ''' Trash bin class '''
    ''' Two class variables all_coordinates and trash_counter store all coridantes of 
    the trash bins and total number of created trashbins respectively '''
    all_coordinates = [] 
    trash_counter = 0
    def __init__(self, map_origin, map_size, map_step):
        '''
        @param map_origin: single value of where does the map has its origin e.g. 0
        @type map_origin: int
        
        @param map_size: single value of where does the map has its end e.g. 100
        @type map_size: int
        
        @param map_step: single value of unit distance between nodes e.g. 10
        @type map_step: int
        '''
        TrashBin.trash_counter += 1
        
        if TrashBin.trash_counter == 1:
            self.X_Y_coordinates = (random.randrange(map_origin + map_step, map_size, map_step), 
                                    random.randrange(map_origin + map_step, map_size, map_step))
            TrashBin.all_coordinates.append(self.X_Y_coordinates)
        else: #here I try to aviod two bins having the same coordiantes, maybe can be done in a smarter way...
            self.X_Y_coordinates = (random.randrange(map_origin, map_size, map_step), 
                                    random.randrange(map_origin, map_size, map_step))
            while self.X_Y_coordinates == TrashBin.all_coordinates[TrashBin.trash_counter - 2] or self.X_Y_coordinates == (0,0):
                self.X_Y_coordinates = (random.randrange(map_origin, map_size, map_step), 
                                        random.randrange(map_origin, map_size, map_step))
            TrashBin.all_coordinates.append(self.X_Y_coordinates)
                
        self.filling_rate = random.randint(1, 10)
        self.initial_level = random.randint(0, 50)
        self.capacity = 50 
        
        print("Trash Bin no. %d, created at: (%d, %d)" % 
              (TrashBin.trash_counter, self.X_Y_coordinates[0], self.X_Y_coordinates[1]))
        
    #methods coming soon...
if __name__ == '__main__':
    pass