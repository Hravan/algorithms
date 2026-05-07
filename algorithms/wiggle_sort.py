from itertools import zip_longest

def wiggle_sort(nums):
    nums.sort()
    n_odd = len(nums) // 2
    
    result = []
    for even, odd in zip_longest(nums[:-n_odd], nums[-n_odd:]):
        result.append(even)
        if odd is not None:
            result.append(odd)
    return result