from typing import List

class Solution:
    """
    This is called Kadane's algorithm, for make it, we need to keep the max value of all the subsecuences
    done untilt the current element and the max value of all the subsecuences done until the current element.

    This time is a little bit more complex, this time we are going to swap values, if the num is negative
    because the positive one becomes negative, and the negative one becomes positive. After that select the
    biggest one.
    """
    def maxProduct(self, nums: List[int]) -> int:
        max_seq= nums[0]
        max_top = nums[0]
        max_negative = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                max_seq, max_negative = max_negative, max_seq
            
            max_seq = max(num, max_seq * num)
            max_negative = min(num, max_negative * num)
        
            max_top = max(max_seq, max_top)
        return max_top