from typing import List

class Solution:
    """
    finding a O(log n)
    """
    def findMin(self, nums: List[int]) -> int:
        start_x = -50001
        end_x = 50001
        while nums:
            mid = (start_x + end_x) // 2
            if mid in nums:
                return mid
            elif mid < nums[0]:
                end_x = mid
            else:
                start_x = mid