from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        mp = defaultdict(list)

        for w in strs:
            ord_w = ''.join(sorted(w))
            mp[ord_w].append(ord_w)

        return mp.values()



solution = Solution()
ans = solution.groupAnagrams(["ate", "tea", "tan"])
