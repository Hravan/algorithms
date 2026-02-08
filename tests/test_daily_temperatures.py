from algorithms.daily_temperatures import day_diff_to_higher


def test_one_day():
    assert day_diff_to_higher([23]) == [0]

def test_two_days_one_higher():
    assert day_diff_to_higher([23, 24]) == [1, 0]

def test_leetcode_1():
    assert day_diff_to_higher([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]

def test_leetcode_2():
    assert day_diff_to_higher([30,40,50,60]) == [1,1,1,0]

def test_leetcode_3():
    assert day_diff_to_higher([30,60,90]) == [1,1,0]
