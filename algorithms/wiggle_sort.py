def wiggle_sort(nums):
    nums.sort()
    n_odd = len(nums) // 2
    
    result = []
    i_even = 0
    i_odd = 0
    for i, _ in enumerate(nums):
        if not i % 2:
            result.append(nums[i_even])
            i_even += 1
        else:
            result.append(nums[-n_odd:][i_odd])
            i_odd += 1
    return result