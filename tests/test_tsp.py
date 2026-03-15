from algorithms.tsp import nearest_neighbour, closest_pair


def test_nearest_neighbour(mocker):
    locations = [-21, -5, -1, 0, 1, 3, 11]
    mocker.patch('random.randrange', return_value=1)
    assert nearest_neighbour(locations) == [-5, -1, 0, 1, 3, 11, -21]


def test_closest_pair():
    locations = [-10, -1, 0]
    assert closest_pair(locations) == [-10, -1, 0]
    locations = [-21, -5, -1, 0, 1, 3, 11]
    assert closest_pair(locations) == [-21, -5, -1, 0, 1, 3, 11]
