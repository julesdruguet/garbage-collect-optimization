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
        '''
        Parametrized constructor of TrashBin class
        '''
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
        self.bin_id = TrashBin.trash_counter


    def increment_trash(self):
        '''
        When this method is called, amount of trash is the bin is increased by the corresponding filling rate
        '''
        if self.current_level + self.filling_rate > self.capacity:
            self.current_level = self.capacity
        else:
            self.current_level += self.filling_rate
        
        print("Trash Bin no. %d, level: %d" % 
              (self.bin_id, self.current_level))     

    def empty_trashbin(self):
        '''
        When this method is called, level of trash, for a given bin is set to 0
        '''
        self.current_level = 0
        
if __name__ == '__main__':
    pass