class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False

solution = Solution()
print(solution.containsDuplicate([x for x in range(10_000_000)]))
