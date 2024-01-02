def twoSum(nums, target):
    nums_dict = {}
    for x, num in enumerate(nums):
        if target-num in nums_dict:
            return [nums_dict[target-num], x]
        nums_dict[num]= x

print(twoSum([3,2,4],6))