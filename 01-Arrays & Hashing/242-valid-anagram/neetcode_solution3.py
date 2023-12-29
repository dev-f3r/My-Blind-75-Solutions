class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("anagram", "nagara"))
