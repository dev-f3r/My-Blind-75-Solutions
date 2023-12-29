from typing import List
from math import prod


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            pre = prod(nums[:i])
            pos = prod(nums[i + 1 :])
            answer.append(pre * pos)

        return answer


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
