import numpy as np
(in progresss)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        x,y,z = -1,-1,-1
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
        for x in range(0, len(nums)-2):
            for y in range(x+1, len(nums)-2):
                z = (0-nums[x]-nums[y])
                aux =[nums[x],nums[y],z]
                if z in nums and aux not in res:
                    res.append(aux)
            used=[]
        return res
