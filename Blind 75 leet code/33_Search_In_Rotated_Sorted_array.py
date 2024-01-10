from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        start_x = -50001
        end_x = 50001
        while nums:
            mid = (start_x + end_x) // 2
            if mid == target:
                return mid
            elif mid < nums[0]:
                end_x = mid
            else:
                start_x = mid
        return -1