from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

class Tsp:

    def create_data_model(self, bins_to_collect):
        """Stores the data for the problem."""
        data = {}
        data['distance_matrix'] = []
        for i in range(len(bins_to_collect)):
            distances_from_i = []
            for j in range(len(bins_to_collect)):
                manhattan_distance = abs(bins_to_collect[i][0]-bins_to_collect[j][0])+abs(bins_to_collect[i][1]-bins_to_collect[j][1])
                distances_from_i.append(manhattan_distance)
            data['distance_matrix'].append(distances_from_i)
        data['num_vehicles'] = 1
        data['depot'] = 0
        return data


    def print_solution(self, manager, routing, assignment):
        """Prints assignment on console."""
        print('Objective: {}'.format(assignment.ObjectiveValue()))
        index = routing.Start(0)
        plan_output = 'Route for vehicle 0:\n'
        route_distance = 0
        route_itinerary = []
        while not routing.IsEnd(index):
            plan_output += ' {} ->'.format(manager.IndexToNode(index))
            route_itinerary.append(manager.IndexToNode(index))
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        plan_output += ' {}\n'.format(manager.IndexToNode(index))
        print(plan_output)
        plan_output += 'Route distance: {}\n'.format(route_distance)
        return route_itinerary, route_distance


    def __init__(self, bins_to_collect):
        """Entry point of the program."""
        # Instantiate the data problem.
        data = self.create_data_model(bins_to_collect)
        print('\n'.join([''.join(['{:15}'.format(item) for item in row]) for row in data['distance_matrix']]))

        # Create the routing index manager.
        manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                               data['num_vehicles'], data['depot'])

        # Create Routing Model.
        routing = pywrapcp.RoutingModel(manager)


        def distance_callback(from_index, to_index):
            """Returns the distance between the two nodes."""
            # Convert from routing variable Index to distance matrix NodeIndex.
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return data['distance_matrix'][from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        # Define cost of each arc.
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

        # Solve the problem.
        assignment = routing.SolveWithParameters(search_parameters)

        # Print solution on console.
        if assignment:
            self.route_itinerary, self.route_distance = self.print_solution(manager, routing, assignment)
