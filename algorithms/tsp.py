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


def closest_pair(locations: list[int]):
    '''Order the locations to visit using the closest pair heuristic.'''
    n_points = len(locations)
    chains = [[location] for location in locations]
    while len(chains) != 1:
        smallest_distance = float('inf')
        for i_chain_a, chain_a in enumerate(chains):
            for i_chain_b, chain_b in enumerate(chains[i_chain_a + 1:], start=i_chain_a+1):
                start_a = chain_a[0]
                end_a = chain_a[-1]
                start_b = chain_b[0]
                end_b = chain_b[-1]
                for k, pair in enumerate([(end_a, start_b), (start_a, start_b), (start_a, end_b), (end_a, end_b)]):
                    current_distance = abs(pair[0] - pair[1])
                    print(current_distance)
                    if current_distance < smallest_distance:
                        i_to_connect_a = i_chain_a
                        i_to_connect_b = i_chain_b
                        i_pair = k
                        smallest_distance = current_distance
        connect_chains(chains, i_to_connect_a, i_to_connect_b, i_pair)
    return chains[0]


def connect_chains(chains, i_chain_a, i_chain_b, i_pair):
    if i_pair == 0:
        connect_chains(chains, i_chain_b, i_chain_a, 1)
    elif i_pair == 1:
        chain_b = chains[i_chain_b][::-1]
        chain_b.extend(chains[i_chain_a])
        chains.append(chain_b)
        for i_chain in sorted([i_chain_a, i_chain_b], reverse=True):
            del chains[i_chain]
    elif i_pair == 2:
        chains[i_chain_b].extend(chains[i_chain_a])
        del chains[i_chain_a]
    elif i_pair == 3:
        chains[i_chain_a].extend(chains[i_chain_b][::-1])
        del chains[i_chain_b]


