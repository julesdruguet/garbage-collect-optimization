# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:15:15 2019

@author: aleks
"""

from map import Map
from trashbin import TrashBin
from tsp import Tsp
from garbage_truck import GarbageTruck
import sys
import json

def import_parameters():
    try:
        path2config = str(sys.argv[1])
        print(path2config)
        params = {}
        with open(path2config) as json_file:
            data = json.load(json_file)
            for name in data:
                if name == 'garbage_center':
                    params[name] = tuple(data[name])
                elif name == 'truck_capacity_bins_no':
                    params['truck_capacity'] = data[name] * params['bin_capacity']
                else:
                    params[name] = data[name]
        return params
    except IndexError:  
        print('Error! Please provide a config file.')

def setup(parameters):
    #creates a list of trashbins of an amount given by amount_of_trash_bins variable
    trashbins = [TrashBin(parameters['map_origin'], parameters['map_size'], parameters['map_step']) for x in range(parameters['amount_of_trash_bins'])]
    truck = GarbageTruck(parameters['garbage_center'], parameters['truck_capacity'], parameters['map_step'])

    #here coordiantes are separted into two lists using get_labeled_bin
    bins_ready_for_pickup, bins_not_ready_for_pickup = get_labeled_bin(trashbins, parameters['threshold'])
    itinerary_coordinates = []

    #create Map instance
    city = Map((parameters['map_size'], parameters['map_size']), parameters['map_step'], bins_ready_for_pickup, bins_not_ready_for_pickup, itinerary_coordinates, parameters['garbage_center'])

    return trashbins, truck, bins_ready_for_pickup, bins_not_ready_for_pickup, itinerary_coordinates, city

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

def redraw_map(city, bins_ready_for_pickup, bins_not_ready_for_pickup, title, *args):
    if len(args ) == 0:
        city.update_trash(bins_ready_for_pickup, bins_not_ready_for_pickup)
        city.show_map(title)
        input("Press Enter to continue...")
    else:
        city.update_trash(bins_ready_for_pickup, bins_not_ready_for_pickup, args[0], args[1])
        city.show_map(title)
        input("Press Enter to continue...")

if __name__ == '__main__':
    parameters = import_parameters()
    print(parameters)
    trashbins, truck, bins_ready_for_pickup, bins_not_ready_for_pickup, itinerary_coordinates, city = setup(parameters)

    #basic simulation
    for x in range(parameters['iterations']):
        if (x % parameters['pickup_iter']) == 0:
            redraw_map(city, bins_ready_for_pickup, bins_not_ready_for_pickup, 'Trash level before the pick up')
            bins_and_center = truck_pickup(trashbins, bins_ready_for_pickup, truck)
            # bins_and_center = bins_ready_for_pickup.copy()
            bins_and_center.insert(0, parameters['garbage_center'])
            route = Tsp(bins_and_center)
            for coordinates_index in route.route_itinerary:
                itinerary_coordinates.append(bins_and_center[coordinates_index])

            redraw_map(city, bins_ready_for_pickup, bins_not_ready_for_pickup, 'Trash level at the pick up', bins_and_center, itinerary_coordinates)

            truck.update_data(route.route_distance)
            truck.print_data()

            # if the trashbin has been collected, empty it
            empty_trashbins(trashbins, itinerary_coordinates)
            bins_ready_for_pickup, bins_not_ready_for_pickup = get_labeled_bin(trashbins, parameters['threshold'])

            redraw_map(city, bins_ready_for_pickup, bins_not_ready_for_pickup, 'Trash level after the pick up')

            #empty truck
            truck.empty_truck()

        increment_trash_in_bins(trashbins)
        bins_ready_for_pickup, bins_not_ready_for_pickup = get_labeled_bin(trashbins, parameters['threshold'])
        redraw_map(city, bins_ready_for_pickup, bins_not_ready_for_pickup, 'Trash level after single incrementation') 

        itinerary_coordinates = []
