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
    bins_not_ready = [single_bin.X_Y_coordinates for single_bin in bins if single_bin.current_level <= thresh]

    return bins_ready, bins_not_ready

def truck_pickup(all_bins, bins_ready, truck):
    all_bins.sort(key=lambda single_bin: single_bin.current_level, reverse=True)
    print([x.current_level for x in all_bins])
    bins_pickedup = []
    bins_not_pickedup = []

    for single_bin in all_bins:
        if single_bin.X_Y_coordinates in bins_ready:
            if truck.isfull == False:
                print(single_bin)
                truck.collect_trash(single_bin.current_level)
                bins_pickedup.append(single_bin.X_Y_coordinates)
            else:
                pass
        else:
            pass
    return bins_pickedup



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
    garbage_center = (0, 0)

    #initial parameters of simulation
    amount_of_trash_bins = 40
    threshold = 25
    truck_capacity = 50 * 50
    # threshold = 0 #base case

    #creates a list of trashbins of an amount given by amount_of_trash_bins variable
    trashbins = [TrashBin(map_origin, map_size, map_step) for x in range(amount_of_trash_bins)]
    truck = GarbageTruck(garbage_center, truck_capacity)

    #here coordiantes are separted into two lists using get_labeled_bin
    bins_ready_for_pickup, bins_not_ready_for_pickup = get_labeled_bin(trashbins, threshold)
    itinerary_coordinates = []

    #create Map instance
    city = Map((map_size, map_size), map_step, bins_ready_for_pickup, bins_not_ready_for_pickup, itinerary_coordinates, garbage_center)
    city.update_trash(bins_ready_for_pickup, bins_not_ready_for_pickup,)
    city.show_map()        
    input("Press Enter to continue...")

    #basic simulation, right now only increase of trash level is visible
    for x in range(20):
        if (x % 3) == 0:
            city.update_trash(bins_ready_for_pickup, bins_not_ready_for_pickup,)
            city.show_map()
            print(bins_ready_for_pickup, 'bins_ready_for_pickup')
            bins_and_center = truck_pickup(trashbins, bins_ready_for_pickup, truck)
            # bins_and_center = bins_ready_for_pickup.copy()
            bins_and_center.insert(0, garbage_center)
            route = Tsp(bins_and_center)
            for coordinates_index in route.route_itinerary:
                itinerary_coordinates.append(bins_and_center[coordinates_index])

            truck.update_data(route.route_distance, map_step)
            truck.print_data()

            # if the trashbin has been collected, empty it
            empty_trashbins(trashbins, itinerary_coordinates)

            #same for the truck
            truck.empty_truck()




        input("Press Enter to continue...")
        city.update_trash(bins_ready_for_pickup, bins_not_ready_for_pickup, bins_and_center, itinerary_coordinates)
        city.show_map()
        increment_trash_in_bins(trashbins)
        bins_ready_for_pickup, bins_not_ready_for_pickup = get_labeled_bin(trashbins, threshold)



        itinerary_coordinates = []
