from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers at the beginning and end of the array
        l, r = 0, len(height) - 1

        # Initialize the variable to store the maximum area
        res = 0

        # Continue the loop until the left pointer is less than the right pointer
        while l < r:
            # Calculate the area between the two pointers and update the maximum area
            area = (r - l) * min(height[l], height[r])

            # Move the pointer pointing to the smaller height towards the center
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

            # Update the maximum area if the current area is greater
            res = max(res, area)

        # Return the maximum area obtained from the two pointers
        return res
