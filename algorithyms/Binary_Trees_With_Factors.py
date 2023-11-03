"""Intuition
Apply memoization, try to calculate the solution, based on previous solutions

Approach
Sort the List: Starting by sorting the list allows us to first consider smaller numbers, which are likely to act as factors for larger numbers.
1.** Memoization with a Dictionary**: Use a dictionary to store the number of trees each number can form. Each entry in the dictionary is built using previously computed solutions.
Iterate and Build Solutions: For each number in the sorted list, consider all previous numbers as potential factors. If both factors are present in the list, build the solution for the current number by adding the product of the solutions of the two factors.
Complexity
Time complexity:
In the worst case: O(n^2)
in the best case: O(n log n)

Space complexity:
O(n) at any case


beats 80% of users
Code
"""
from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dict_sol = {num: 1 for num in arr}
        num_set = set(arr)
        for i, num in enumerate(arr):
            for j in range(i):
                factor = arr[j]
                if num % factor == 0 and num // factor in num_set:
                    dict_sol[num] += dict_sol[factor] * dict_sol[num // factor]
                    
        return sum(dict_sol.values()) % MOD