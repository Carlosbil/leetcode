from typing import List

class Solution:
    """
    Multiply all the elements in the array except the current one, inspired in:
    https://www.youtube.com/watch?v=5bS636lE_R0&t=1s
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        sol = [1] * length
        left, right = 1, nums[-1]
        for i in range(length):
            sol[i] = left
            left *= nums[i]

        for i in range(length - 2, -1, -1):
            sol[i] *= right
            right *= nums[i]
            
        return sol