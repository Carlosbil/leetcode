"""Intuition
This could be resolve directly

Approach
We will iterate through both arrays, left and right. For each ant in the left array, its position gives the time it will take to fall off the left end of the plank. For each ant in the right array, n minus its position gives the time it will take to fall off the right end of the plank. The answer to the problem is the maximum of these times.

Complexity
Time complexity:
O(L+R)

Space complexity:
O(1)

Code"""
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        max_left = max(left) if left else 0
        max_right = n - min(right) if right else 0
        return max(max_left, max_right)
        