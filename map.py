import numpy as np
#import random
import matplotlib.pyplot as plt



class Map:
    '''
    Map class, it has mainly visualization purpose
    '''
    def __init__(self, input_size, step, bins_ready_to_pickup, bins_not_ready_to_pickup, itinerary_coordinates, garbage_center):
        '''
        @param input_size: single value of hwo big is our map/city end e.g. input_size = 100, will create a 100x100 map
        @type input_size: int

        @param step: single value of unit distance between nodes e.g. 10
        @type step: int

        @param bins_ready_to_pickup: list of tuples contining coordiantes bins, which are ready for pick up
        @type bins_ready_to_pickup: list

        @param bins_not_ready_to_pickup: list of tuples contining coordiantes bins, which are NOT ready for pick up
        @type bins_not_ready_to_pickup: list
        '''

        '''
        Parametrized constructor of TrashBin class
        '''
        self.input_size = input_size
        self.step = step

        self.pickedup_X = []
        self.pickedup_X = []
        self.ready_to_pickup_X = [coor[0] for coor in bins_ready_to_pickup]
        self.ready_to_pickup_Y = [coor[1] for coor in bins_ready_to_pickup]
        self.not_ready_to_pickup_X = [coor[0] for coor in bins_not_ready_to_pickup]
        self.not_ready_to_pickup_Y = [coor[1] for coor in bins_not_ready_to_pickup]
        self.itinerary_coordinates = itinerary_coordinates
        self.garbage_center = garbage_center

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
        #        fig, ax = plt.subplots()

        self.fig, self.ax = plt.subplots()
        self.annotations_list = []
        self.fig.show()

    def update_trash(self, bins_ready_to_pickup, bins_not_ready_to_pickup, bins_pickedup=[], itinerary_coordinates=[]):
        '''
        @param bins_ready_to_pickup: list of tuples contining coordiantes bins, which are ready for pick up
        @type bins_ready_to_pickup: list

        @param bins_not_ready_to_pickup: list of tuples contining coordiantes bins, which are NOT ready for pick up
        @type bins_not_ready_to_pickup: list
        '''

        '''
        This method updates the the data, which needs to be plotted
        '''
        self.ready_to_pickup_X = [coor[0] for coor in bins_ready_to_pickup]
        self.ready_to_pickup_Y = [coor[1] for coor in bins_ready_to_pickup]
        self.pickedup_X = [coor[0] for coor in bins_pickedup]
        self.pickedup_Y = [coor[1] for coor in bins_pickedup]
        self.not_ready_to_pickup_X = [coor[0] for coor in bins_not_ready_to_pickup]
        self.not_ready_to_pickup_Y = [coor[1] for coor in bins_not_ready_to_pickup]
        self.itinerary_coordinates = itinerary_coordinates

    def show_map(self):
        '''
        This method adds scatter and grid lines to the plot
        '''

        #dots setting
        self.ax.scatter(self.ready_to_pickup_X, self.ready_to_pickup_Y, color = 'red')
        self.ax.scatter(self.pickedup_X, self.pickedup_Y, color = 'yellow')
        self.ax.scatter(self.not_ready_to_pickup_X, self.not_ready_to_pickup_Y, color = 'green')
        self.ax.scatter(self.garbage_center[0], self.garbage_center[1], color = 'blue', s=144)

        #grid setting
        self.major_ticks = np.arange(0, self.input_size[0], self.step)
        self.ax.set_xticks(self.major_ticks)
        self.ax.set_yticks(self.major_ticks)
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.grid(which='both')
        self.ax.grid(True)

        # Remove previous annotations
        for i, a in enumerate(self.annotations_list):
            a.remove()
        self.annotations_list[:] = []

        # Annotate pick up order
        for i in range(len(self.itinerary_coordinates)):
            annotation = self.ax.annotate(i, (self.itinerary_coordinates[i][0], self.itinerary_coordinates[i][1]))
            self.annotations_list.append(annotation)

        #updates plot instead of creating a new one
        self.fig.canvas.draw()
