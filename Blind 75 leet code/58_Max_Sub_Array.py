from typing import List

class Solution:
    """
    This is called Kadane's algorithm, for make it, we need to keep the max value of all the subsecuences
    done untilt the current element and the max value of all the subsecuences done until the current element
    """
    def maxSubArray(self, nums: List[int]) -> int:
        max_seq= nums[0]
        max_top = nums[0]
        for num in nums[1:]:
            max_seq = max(num, max_seq + num)
            max_top = max(max_seq, max_top)
        return max_top