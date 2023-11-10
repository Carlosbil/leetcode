class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dif_x = abs(fx-sx)  # Compute the horizontal distance between the start and finish.
        dif_y = abs(fy-sy)  # Compute the vertical distance between the start and finish.

        # If both distances are zero and time is also zero, you are already at the destination.
        if dif_x == 0 and dif_y == 0 and t == 0:
            return True

        # If both distances are zero but time is 1, you cannot stay at the destination because you must move every second.
        if dif_x == 0 and dif_y == 0 and t == 1:
            return False

        # If the horizontal or vertical distance is greater than the time available, you cannot reach the destination in time.
        # Otherwise, it is assumed you can reach the destination or move around it within the given time.
        return False if dif_x > t or dif_y > t else True 

            