from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        sol = nums[k]
        i, j = k, k
        minim = nums[k]
        
        while i > 0 or j < len(nums) - 1:

            # move to left or right, if it is not posible to move to one of them
            # move to the other one 
            if i == 0:
                j += 1
            elif j == len(nums) - 1:
                i -= 1
            #if it is possible, move to the greater than 
            elif nums[i-1] > nums[j+1]:
                i -= 1
            else:
                j += 1
            minim = min(minim, nums[i], nums[j])
            sol = max(sol, minim * (j - i + 1))
        
        return sol


sol = Solution()
print (sol.maximumScore([1,4,3,7,4,5], 3))