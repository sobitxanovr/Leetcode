def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    for i in range(len(nums)):
        k = i + 1
        while k < len(nums):
            if nums[i] + nums[k] == target:
                result.append(i)
                result.append(k)
            k += 1
    return result


print(twoSum([2, 7, 2, 15], 9))
