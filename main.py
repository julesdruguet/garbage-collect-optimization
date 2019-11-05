# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:15:15 2019

@author: aleks
"""

from map import Map
from trashbin import TrashBin
from tsp import Tsp


def get_labeled_bin(bins, thresh):
    bins_ready = [single_bin.X_Y_coordinates for single_bin in bins if single_bin.current_level > thresh]
    bins_notready = [single_bin.X_Y_coordinates for single_bin in bins if single_bin.current_level <= thresh]

    return bins_ready, bins_notready

if __name__ == '__main__':
    map_origin = 0
    map_size = 1000
    map_step = 100
    garbage_center = (0, 0)

    #initial parameters of simulation
    amount_of_trash_bins = 5
    threshold = 25
    # threshold = 0 #base case

    #creates a list of trashbins of an amount given by amount_of_trash_bins variable
    trashbins = [TrashBin(map_origin, map_size, map_step) for x in range(amount_of_trash_bins)]

    #here coordiantes are separted into two lists using get_labeled_bin
    bins_ready_for_pickup, bins_not_ready_for_pickup = get_labeled_bin(trashbins, threshold)
    itinerary_coordinates = []

    #create Map instance
    city = Map((map_size, map_size), map_step, bins_ready_for_pickup, bins_not_ready_for_pickup, itinerary_coordinates, garbage_center)

    #basic simulation, right now only increase of trash level is visible
    for x in range(10):

        if (x % 3) == 0:
            bins_and_center = bins_ready_for_pickup.copy()
            bins_and_center.insert(0, garbage_center)
            route = Tsp(bins_and_center)
            for coordinates_index in route.route_itinerary:
                itinerary_coordinates.append(bins_and_center[coordinates_index])
            # if the trashbin has been collected, empty it
            for trashbin in trashbins:
                if trashbin.X_Y_coordinates in itinerary_coordinates:
                    trashbin.empty_trashbin()

        city.update_trash(bins_ready_for_pickup, bins_not_ready_for_pickup, itinerary_coordinates)
        city.show_map()
        input("Press Enter to continue...")

        for trashbin in trashbins:
            trashbin.increment_trash()

        bins_ready_for_pickup, bins_not_ready_for_pickup = get_labeled_bin(trashbins, threshold)

        itinerary_coordinates = []
