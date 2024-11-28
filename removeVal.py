def removeVal(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            n = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = val

ls = [5,3,6,7,8,3,4]
removeVal(ls,3)

for i in ls:
    print(i)
