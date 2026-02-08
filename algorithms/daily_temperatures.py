# https://leetcode.com/problems/daily-temperatures/description/

def day_diff_to_higher(temperatures: list[int]) -> list[int]:
    day_differences: list[int] = []
    for i, temperature in enumerate(temperatures):
        day_differences.append(0)
        for j, future_temperature in enumerate(temperatures[i+1:], i + 1):
            if future_temperature > temperature:
                day_differences[i] = j - i
                break
    return day_differences
