from algorithms.wiggle_sort import wiggle_sort

def test_empty_list():
    assert wiggle_sort([]) == []

def test_two_numbers():
    assert wiggle_sort([2, 1]) == [1, 2]

def test_three_numbers():
    assert wiggle_sort([3, 2, 1]) == [1, 3, 2]

def test_five_numbers():
    assert wiggle_sort([5, 4, 3, 2, 1]) == [1, 4, 2, 5, 3]
