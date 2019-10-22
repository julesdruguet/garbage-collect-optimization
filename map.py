# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import random
import matplotlib.pyplot as plt
 

class Map:
    def __init__(self, input_size, step):
        self.input_size = input_size
        self.step = step
        self.points_x = []
        self.points_y = []
        
        for x in range (0, self.input_size[0], self.step): 
            for y in range(0, self.input_size[0], self.step):
                self.points_x.append(x)
                self.points_y.append(y)    
#        self.points_x = np.empty(0)
#        self.points_y = np.empty(0)
#        for x in range(0, self.input_size[0], self.step):
#            self.points_x = np.append(self.points_x, x) 
#            for y in range(0, self.input_size[0], self.step):
#                self.points_y = np.append(self.points_y, y)                     
        
    def draw(self):
        fig, ax = plt.subplots()
        ax.scatter(self.points_x, self.points_y)
        major_ticks = np.arange(0, self.input_size[0], self.step)
        ax.set_xticks(major_ticks)
        ax.set_yticks(major_ticks)
        ax.grid(which='both')
        ax.grid(True)
        fig.tight_layout()
        
        plt.show()
        
if __name__ == '__main__':
    city = Map((100,100), 10)
    city.draw()