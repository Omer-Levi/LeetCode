def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 1:
        return True
    if nums[0] == 0:
        return False
    index = nums[0]
    if index >= len(nums):
        return False
    
    while True:
        if index == (len(nums) - 1):
            return True
        if index >= len(nums):
            return False
        if nums[index] == 0:
            return False
        index += nums[index]

print(canJump([1,2,3]))