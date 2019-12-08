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
from time import gmtime, strftime
import csv

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
    trashbins = [TrashBin(parameters['map_origin'], parameters['map_size'], parameters['map_step'], parameters['bin_capacity']) for x in range(parameters['amount_of_trash_bins'])]

    trucks = [GarbageTruck(parameters['garbage_center'], parameters['truck_capacity'], parameters['map_step']) for x in range(parameters['num_vehicles'])]

    #here coordiantes are separted into two lists using get_labeled_bin
    bins_ready_for_pickup, bins_not_ready_for_pickup = get_labeled_bin(trashbins, parameters['threshold'])
    itinerary_coordinates = []

    #create Map instance
    city = Map((parameters['map_size'], parameters['map_size']), parameters['map_step'], bins_ready_for_pickup, bins_not_ready_for_pickup, itinerary_coordinates, parameters['garbage_center'])

    return trashbins, trucks, bins_ready_for_pickup, bins_not_ready_for_pickup, itinerary_coordinates, city

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

def log_data(data, x):
    # print(data, x)
    name = './logs/log_' + x + '_' + strftime('%Y-%m-%d-%H-%M.csv')
    myFile = open(name, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)

    print("Writing complete")



if __name__ == '__main__':
    parameters = import_parameters()
    print(parameters)
    trashbins, trucks, bins_ready_for_pickup, bins_not_ready_for_pickup, itinerary_coordinates, city = setup(parameters)
    data = [['iteration', 'truck id', 'distance', 'time', 'trash collected']]
    trashbin_data = [['iteration', 'bin id', 'filling rate', 'level' 'time since last pick up']]

    # simulation
    for x in range(parameters['iterations']):
        if (x % parameters['pickup_iter']) == 0:
            redraw_map(city, bins_ready_for_pickup, bins_not_ready_for_pickup, 'Trash level before the pick up')
            # bins_and_center = truck_pickup(trashbins, bins_ready_for_pickup, truck)
            bins_and_center = bins_ready_for_pickup.copy()
            bins_and_center.insert(0, parameters['garbage_center'])
            vehicles_routing = Tsp(bins_and_center, parameters['num_vehicles'])
            i = 0
            while i < len(vehicles_routing.routes):
                route = vehicles_routing.routes[i]
                itinerary_coordinates.append([]);
                for coordinates_index in route[1]:
                    itinerary_coordinates[i].append(bins_and_center[coordinates_index])
                i += 1

            redraw_map(city, bins_ready_for_pickup, bins_not_ready_for_pickup, 'Trash level at the pick up', bins_and_center, itinerary_coordinates)

            for index, truck in enumerate(trucks):
                truck.update_truck_data(vehicles_routing.routes[index][0])
                data.append(truck.get_truck_data(x))

            # if the trashbin has been collected, empty it
            for coordinates in itinerary_coordinates:
                empty_trashbins(trashbins, coordinates)

            bins_ready_for_pickup, bins_not_ready_for_pickup = get_labeled_bin(trashbins, parameters['threshold'])
            redraw_map(city, bins_ready_for_pickup, bins_not_ready_for_pickup, 'Trash level after the pick up')

            #empty truck
            for truck in trucks:
                truck.empty_truck()

            
            for b in trashbins:
                trashbin_data.append([x, b.bin_id, b.filling_rate, b.current_level, b.time_since_last_collection])

        increment_trash_in_bins(trashbins)
        bins_ready_for_pickup, bins_not_ready_for_pickup = get_labeled_bin(trashbins, parameters['threshold'])
        redraw_map(city, bins_ready_for_pickup, bins_not_ready_for_pickup, 'Trash level after single incrementation')

        for b in trashbins:
            trashbin_data.append([x, b.bin_id, b.filling_rate, b.current_level, b.time_since_last_collection])

        itinerary_coordinates = []
    # log_data(data, 'trucks')
    # log_data(trashbin_data, 'bins')