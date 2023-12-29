class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}

        for l in s:
            if l in hash:
                hash[l] += 1
            else:
                hash[l] = 1

        print(hash)

        for l in t:
            if not(l in hash): return False
            if l in hash:
                if hash[l] == 0: return False
                hash[l] -= 1

        for l in hash:
            if hash[l] != 0: return False

        return True

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("anagram", "nagara"))
