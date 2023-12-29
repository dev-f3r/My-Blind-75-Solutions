from typing import List
import pdb


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1] * n

        pdb.set_trace()
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        posfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= posfix
            posfix *= nums[i]

        return res


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
