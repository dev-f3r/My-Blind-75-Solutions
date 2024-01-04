import pdb


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()

        r = 0
        res = 0
        while r < len(s):
            pdb.set_trace()
            if s[r] in substr:
                substr.remove(s[r])

            substr.add(s[r])
            r += 1

            res = max(res, len(substr))

        return res


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
