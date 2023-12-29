class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_hash = {}
        t_hash = {}

        for i in range(len(s)):
            if s[i] in s_hash:
                s_hash[s[i]] += 1
            else:
                s_hash[s[i]] = 1

            if t[i] in t_hash:
                t_hash[t[i]] += 1
            else:
                t_hash[t[i]] = 1
        
        print(s_hash)
        print(t_hash)

        if s_hash != t_hash: return False

        return True


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
# print(solution.isAnagram("anagram", "nagara"))
print(solution.isAnagram("aabbbb", "aaaabb"))
