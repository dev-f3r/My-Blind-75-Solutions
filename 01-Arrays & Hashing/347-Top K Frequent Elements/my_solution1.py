class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mp = {}

        for n in nums:
            mp[n] = mp.get(n, 0) + 1

        return list(dict(sorted(mp.items(), key=lambda val: val[1])).keys())[-k:]


solution = Solution()
ans = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(ans)
