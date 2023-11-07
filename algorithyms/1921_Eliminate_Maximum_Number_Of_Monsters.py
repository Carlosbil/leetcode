from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Calculate the time it will take for each monster to reach the city
        reach_times = [dist[i] / speed[i] for i in range(len(dist))]
        # Sort the reach times to eliminate monsters in the right order
        reach_times.sort()
        # Initialize the count of monsters eliminated
        monsters_eliminated = 0
        # Iterate over the sorted reach times
        for i, reach_time in enumerate(reach_times):
            # If the current monster reaches the city before or at the current time,
            # we cannot eliminate it, so break the loop
            if reach_time <= i:
                break
            # Otherwise, we can eliminate the monster and increment the count
            monsters_eliminated += 1
        
        return monsters_eliminated

# The function can now be used as follows:
# solution = Solution()
# print(solution.eliminateMaximum([1,3,4], [1,1,1])) # Output should be 3
