class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        map = {}
        for n in nums:
            if map.get(n, False):
                return True
            else:
                map[n] = True
            # print(map)
        return False

solution = Solution()
print(solution.containsDuplicate([x for x in range(10_000_000)]))

