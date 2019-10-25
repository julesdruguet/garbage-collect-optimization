# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:15:15 2019

@author: aleks
"""

from map import Map
from trashbin import TrashBin
import msvcrt


if __name__ == '__main__':
    #initial parameters of simulation
    map_origin = 0
    map_size = 1000
    map_step = 100
    amount_of_trash_bins = 50
    threshold = 25

    #creates a list of trashbins of an amount given by amount_of_trash_bins variable 
    trashbins = [TrashBin(map_origin, map_size, map_step) for x in range(amount_of_trash_bins)]

    #here coordiantes are separted into two lists 
    bins_ready_for_pickup = [trashbin.X_Y_coordinates for trashbin in trashbins if trashbin.current_level > threshold]
    bins_not_ready_for_pickup = [trashbin.X_Y_coordinates for trashbin in trashbins if trashbin.current_level <= threshold]
    
    #create Map instance
    city = Map((map_size, map_size), map_step, bins_ready_for_pickup, bins_not_ready_for_pickup)
    
    #basic simulation, right now only increase of trash level is visible 
    for x in range(10):
        city.update_trash(bins_ready_for_pickup, bins_not_ready_for_pickup)
        city.show_map()
        input("Press Enter to continue...")

        for trashbin in trashbins:
            trashbin.increment_trash()
        bins_ready_for_pickup = [trashbin.X_Y_coordinates for trashbin in trashbins if trashbin.current_level > threshold]
        bins_not_ready_for_pickup = [trashbin.X_Y_coordinates for trashbin in trashbins if trashbin.current_level <= threshold]
        
