from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

class Tsp:

    def create_data_model(self, bins_to_collect, num_vehicles):
        """Stores the data for the problem."""
        data = {}
        data['distance_matrix'] = []
        for i in range(len(bins_to_collect)):
            distances_from_i = []
            for j in range(len(bins_to_collect)):
                manhattan_distance = abs(bins_to_collect[i][0]-bins_to_collect[j][0])+abs(bins_to_collect[i][1]-bins_to_collect[j][1])
                distances_from_i.append(manhattan_distance)
            data['distance_matrix'].append(distances_from_i)
        data['num_vehicles'] = num_vehicles
        data['depot'] = 0
        return data


    def print_solution(self, data, manager, routing, solution):
        """Prints solution on console."""
        max_route_distance = 0
        solution_matrix = []
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            # distance, route
            solution_matrix.append([0, []])
            plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
            route_distance = 0
            while not routing.IsEnd(index):
                plan_output += ' {} -> '.format(manager.IndexToNode(index))
                solution_matrix[vehicle_id][1].append(manager.IndexToNode(index))
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(
                    previous_index, index, vehicle_id)
            plan_output += '{}\n'.format(manager.IndexToNode(index))
            plan_output += 'Distance of the route: {}m\n'.format(route_distance)
            #print(plan_output)
            max_route_distance = max(route_distance, max_route_distance)
            solution_matrix[vehicle_id][0] = route_distance
        #print('Maximum of the route distances: {}m'.format(max_route_distance))
        print(solution_matrix)
        return solution_matrix

    def __init__(self, bins_to_collect, num_vehicles):
        """Entry point of the program."""
        # Instantiate the data problem.
        data = self.create_data_model(bins_to_collect, num_vehicles)

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

        # Add Distance constraint.
        dimension_name = 'Distance'
        routing.AddDimension(
            transit_callback_index,
            0,  # no slack
            3000,  # vehicle maximum travel distance
            True,  # start cumul to zero
            dimension_name)
        distance_dimension = routing.GetDimensionOrDie(dimension_name)
        distance_dimension.SetGlobalSpanCostCoefficient(100)


        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

        # Solve the problem.
        solution = routing.SolveWithParameters(search_parameters)

        # Print solution on console.
        if solution:
            self.routes = self.print_solution(data, manager, routing, solution)
