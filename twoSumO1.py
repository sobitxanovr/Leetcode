def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    res = []
    d = dict()
    d[nums[0]] = 0
    for i in range(1, len(nums)):
        if (target - nums[i]) in d.keys():
            res.append(d[(target - nums[i])])
            res.append(i)
            return res
        else:
            d[nums[i]] = i
    return res


print(twoSum([3,2,4], 6))
