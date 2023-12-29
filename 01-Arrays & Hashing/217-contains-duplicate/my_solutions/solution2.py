class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        sort = sorted(nums)
        for i, n in enumerate(sort):
            if i == len(sort) - 1: return False
            if n == sort[i + 1]: return True

        return False

solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))
print(solution.containsDuplicate([1,2,3,4]))
