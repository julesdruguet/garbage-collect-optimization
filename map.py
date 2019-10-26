import numpy as np
#import random
from trashbin import TrashBin
from tsp import Tsp
import matplotlib.pyplot as plt



class Map:

    threshold = 25

    ''' Map class '''
    def __init__(self, input_size, step, bins_coor, itinerary_coordinates):
        self.input_size = input_size
        self.step = step
        self.bins_x = [coor[0] for coor in bins_coor]
        self.bins_y = [coor[1] for coor in bins_coor]
        self.itinerary_coordinates = itinerary_coordinates

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

        # Draws the route
        route = plt.step([coor[0] for coor in self.itinerary_coordinates], [coor[1] for coor in self.itinerary_coordinates], 'r-', linewidth=1)

        ax.scatter(self.bins_x, self.bins_y)
        for i in range(len(self.itinerary_coordinates)):
            ax.annotate(i, (self.itinerary_coordinates[i][0], self.itinerary_coordinates[i][1]))

        major_ticks = np.arange(0, self.input_size[0], self.step)
        ax.set_xticks(major_ticks)
        ax.set_yticks(major_ticks)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.grid(which='both')
        ax.grid(True)
#        fig.tight_layout()

        plt.show()


if __name__ == '__main__':
    map_origin = 0
    map_size = 3000
    map_step = 30
    amount_of_trash_bins = 50
    trashbins = [TrashBin(map_origin, map_size, map_step) for x in range(amount_of_trash_bins)]

    trash_bins_to_collect = []
    # Select trash bins above the set threshold
    for bin in trashbins:
        if bin.current_level > Map.threshold:
            trash_bins_to_collect.append(bin.X_Y_coordinates)

    route = Tsp(trash_bins_to_collect)
    itinerary_coordinates = []
    for coordinates_index in route.route_itinerary:
        itinerary_coordinates.append(trash_bins_to_collect[coordinates_index])

    bins_coor = trashbins[0].all_coordinates
    city = Map((map_size, map_size), map_step, bins_coor, itinerary_coordinates)
    city.draw()
