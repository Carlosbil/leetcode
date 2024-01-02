"""
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Ez matematical aprroach
# Approach
<!-- Describe your approach to solving the problem. -->
If the number is in target, add push, if not, push, pop to the sol array
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(n)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(n)
# Code
"""
from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        sol = []
        for x in range(1, n+1):
            sol.append("Push")
            if x not in target:
                sol.append("Pop")
            if x == target[-1]:
                break
        return sol


