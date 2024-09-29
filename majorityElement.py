
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dicNum = dict()

    for i in nums:
        if i in dicNum:
            dicNum[i] += 1
        else:
            dicNum[i] = 1
    max_val = max(list(dicNum.values()))
    index = list(dicNum.values()).index(max_val)
    ls_key = list(dicNum)
    return ls_key[index]



nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
    
    