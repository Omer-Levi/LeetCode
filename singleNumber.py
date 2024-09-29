def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    answer = 0
    for num in nums:
        answer ^= num
    return answer
        

ls = [-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]
ls1 = [4,1,2,1,2]
ls2 = [4,1,2,1,1]
print(singleNumber(ls))
# print(ls1-ls2)