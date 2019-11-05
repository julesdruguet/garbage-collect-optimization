# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:15:15 2019

@author: aleks
"""

from map import Map
from trashbin import TrashBin
from tsp import Tsp
from garbage_truck import GarbageTruck


def get_labeled_bin(bins, thresh):
    bins_ready = [single_bin.X_Y_coordinates for single_bin in bins if single_bin.current_level > thresh]
    bins_notready = [single_bin.X_Y_coordinates for single_bin in bins if single_bin.current_level <= thresh]
    total = 0
    for single_bin in bins:
        if single_bin.X_Y_coordinates in bins_ready:
            total += single_bin.current_level

    return bins_ready, bins_notready, total

def empty_trashbins(bins, itinerary_coordinates):
    for trashbin in trashbins:
        if trashbin.X_Y_coordinates in itinerary_coordinates:
            trashbin.empty_trashbin()

def increment_trash_in_bins(bins):
    for trashbin in trashbins:
        trashbin.increment_trash()  



if __name__ == '__main__':
    map_origin = 0
    map_size = 1000
    map_step = 100
    
    #initial parameters of simulation
    amount_of_trash_bins = 50
    threshold = 25
    # threshold = 0 #base case

    #creates a list of trashbins of an amount given by amount_of_trash_bins variable
    trashbins = [TrashBin(map_origin, map_size, map_step) for x in range(amount_of_trash_bins)]
    trucks = [GarbageTruck((0,0))]

    #here coordiantes are separted into two lists using get_labeled_bin
    bins_ready_for_pickup, bins_not_ready_for_pickup, total_trash = get_labeled_bin(trashbins, threshold)
    itinerary_coordinates = []

    #create Map instance
    city = Map((map_size, map_size), map_step, bins_ready_for_pickup, bins_not_ready_for_pickup, itinerary_coordinates)

    #basic simulation, right now only increase of trash level is visible
    for x in range(10):

        if (x % 3) == 0:

            route = Tsp(bins_ready_for_pickup)
            print("%d" % total_trash)

            # exit()
            for coordinates_index in route.route_itinerary:
                itinerary_coordinates.append(bins_ready_for_pickup[coordinates_index])
            # if the trashbin has been collected, empty it
            empty_trashbins(trashbins, itinerary_coordinates)

        city.update_trash(bins_ready_for_pickup, bins_not_ready_for_pickup, itinerary_coordinates)
        city.show_map()
        input("Press Enter to continue...")
        increment_trash_in_bins(trashbins)


        bins_ready_for_pickup, bins_not_ready_for_pickup, total_trash = get_labeled_bin(trashbins, threshold)

        itinerary_coordinates = []
