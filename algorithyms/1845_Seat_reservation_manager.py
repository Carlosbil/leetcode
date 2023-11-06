"""# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Create a heapd to just pop and add elements in order
# Approach
<!-- Describe your approach to solving the problem. -->
Create a heapd to just pop and add elements in order

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(nlog(n))
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(n)
# Code
```"""
import heapq

class SeatManager:

    def __init__(self, n: int):
        # create a heap
        self.available_seats = list(range(1, n + 1))
        heapq.heapify(self.available_seats)

    def reserve(self) -> int:
        # pop head 
        return heapq.heappop(self.available_seats)

    def unreserve(self, seatNumber: int) -> None:
        # add in order
        heapq.heappush(self.available_seats, seatNumber)