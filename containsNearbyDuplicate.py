def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    nums_index = {}
    for i in range(len(nums)):
        if nums[i] in nums_index and i - nums_index[nums[i]] <= k:
            return True
        nums_index[nums[i]] = i
    return False

print(containsNearbyDuplicate([1,0,1,1],1))
