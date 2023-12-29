class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of the two strings are different
        if len(s) != len(t):
            return False

        # Create dictionaries to store character counts for each string
        countS, countT = {}, {}

        # Iterate through each character in the first string (s)
        for i in range(len(s)):
            # Increment the count of the current character in countS
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # Increment the count of the current character in countT
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Iterate through unique characters in countS
        for c in countS:
            # Check if the count of the current character in countS
            # is different from the count in countT (using get to handle
            # cases where the character is not present in countT)
            if countS[c] != countT.get(c, 0):
                # If counts are different, the strings are not anagrams
                return False

        # If the loop completes without returning, the strings are anagrams
        return True
