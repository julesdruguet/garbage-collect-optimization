# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#import random
from trashbin import TrashBin
import matplotlib.pyplot as plt
 

class Map:
    ''' Map class '''
    def __init__(self, input_size, step, bins_coor):
        self.input_size = input_size
        self.step = step
        self.bins_x = [coor[0] for coor in bins_coor]
        self.bins_y = [coor[1] for coor in bins_coor]
        
        
        
        
#        for x in range (0, self.input_size[0], self.step): 
#            for y in range(0, self.input_size[0], self.step):
#                self.points_x.append(x)
#                self.points_y.append(y)    
#        self.points_x = np.empty(0)
#        self.points_y = np.empty(0)
#        for x in range(0, self.input_size[0], self.step):
#            self.points_x = np.append(self.points_x, x) 
#            for y in range(0, self.input_size[0], self.step):
#                self.points_y = np.append(self.points_y, y)                     
        
    def draw(self):
#        fig, ax = plt.subplots()
        
        ax = plt.subplot()
        
        ax.scatter(self.bins_x, self.bins_y)

        major_ticks = np.arange(0, self.input_size[0], self.step)
        ax.set_xticks(major_ticks)
        ax.set_yticks(major_ticks)
        ax.grid(which='both')
        ax.grid(True)
#        fig.tight_layout()
        
        plt.show()
       
        
if __name__ == '__main__':
    map_origin = 0
    map_size = 1000
    map_step = 100
    amount_of_trash_bins = 50
    trashbins = [TrashBin(map_origin, map_size, map_step) for x in range(amount_of_trash_bins)]
    bins_coor = trashbins[0].all_coordinates
    city = Map((map_size, map_size), map_step, bins_coor)
    city.draw()