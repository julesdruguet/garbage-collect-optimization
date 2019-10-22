import mlrose
import numpy as np

class PathFinder:
    ''' Tools to calculate the truck routes '''
    ''' It is assumed that travel between each pair of trash bins is possible
    and that the distance between the pairs of trash bins is the Euclidean
    distance '''

    def __init__(self, bins_to_collect):
        '''
        @param bins_to_collect: ordered list of coordinates, i.e array of pairs of integers
        @type bins_to_collect: numpy array
        '''
        self.bins_to_collect = bins_to_collect
        distances = []
        ''' Calculate the Manhattan distances between each bins '''
        for i in range(len(bins_to_collect)-1):
            for j in range(i+1, len(bins_to_collect)):
                manhattan_distance = abs(bins_to_collect[i][0]-bins_to_collect[j][0])+abs(bins_to_collect[i][1]-bins_to_collect[j][1])
                tuple = (i, j, manhattan_distance)
                distances.append(tuple)

        '''
        The class TravellingSales can take coordinates as a parameter but it
        then calculate the fitness with the Euclidian distances instead of
        Manhattan distances
        '''
        self.fitness = mlrose.TravellingSales(distances = distances)
        self.problem_fit = mlrose.TSPOpt(length = len(bins_to_collect), fitness_fn = self.fitness, maximize=False)

    def solve(pop_size = 200, mutation_prob = 0.1, max_attempts = 10, max_iters=inf):
        '''
        @param pop_size: Size of population to be used in genetic algorithm
        @type pop_size: int
        @param mutation_prob: Probability of a mutation at each element of the state vector during reproduction, expressed as a value between 0 and 1
        @type mutation_prob: float
        @param max_attempts: Maximum number of attempts to find a better state at each step
        @type max_attempts: int
        @param max_iters: Maximum number of iterations of the algorithm
        @type max_iters: inf
        '''

        '''
        best_state is the order of the solution for the route
        best_fitness is the length of the best route
        If random_state is a positive integer, random_state is the seed used by
        np.random.seed(); otherwise, the random seed is not set
        '''
        best_state, best_fitness = mlrose.genetic_alg(self.problem_fit, random_state = 2)

        best_route = []
        for coordinates_index in best_state:
            best_route.append(self.bins_to_collect[coordinates_index])
            
        return best_route, best_fitness
