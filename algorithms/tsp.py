# Exercise 1-30, page 29
import random


def nearest_neighbour(locations: list[int]) -> list[int]:
    '''Order the locations to visit using the nearest neighbour heuristic.
       The first location is chosen at random.'''
    location_order = []
    initial_location_index = random.randrange(len(locations))
    location_order.append(locations.pop(initial_location_index))
    while locations:
        min_diff = float('inf')
        min_index = -1
        for i, location in enumerate(locations):
            if (current_diff := abs(location - location_order[-1])) < min_diff:
                min_diff = current_diff
                min_index = i
        location_order.append(locations.pop(min_index))
    return location_order