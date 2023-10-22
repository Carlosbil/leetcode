class Solution:
    def fibonacci_efficient(self ,n):
        if n == 0:
            return 0
        if n == 1 :
            return 1
        elif n == 2:
            return 2
        else:
            prev, last = 1,2
            for _ in range(3,n+1):
                current = prev + last
                prev,last = last, current
            return last

    def climbStairs(self, n: int) -> int:
        return self.fibonacci_efficient(n)