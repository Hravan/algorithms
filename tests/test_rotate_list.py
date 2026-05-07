from algorithms.rotate_list import rotate_list

def test_empty_list():
    assert rotate_list([]) == []

def test_rotate_1_element():
    assert rotate_list([1]) == [1]

def test_rotate_2_elements_by_1():
    assert rotate_list([1, 2]) == [2, 1]

def test_rotate_3_elements_by_1():
    assert rotate_list([1, 2, 3]) == [3, 1, 2]

def test_rotate_3_elements_by_2():
    assert rotate_list([1, 2, 3], k=2) == [2, 3, 1]
