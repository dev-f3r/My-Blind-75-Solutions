from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE
        res = 0

        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area = (r - l) * min(height[l], height[r]))
                res = max(res, area)

        return res
