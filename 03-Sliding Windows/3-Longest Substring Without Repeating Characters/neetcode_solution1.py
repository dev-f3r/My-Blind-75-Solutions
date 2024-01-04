class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a set to store unique characters in the current substring
        charSet = set()

        # Initialize pointers for the left and right ends of the substring
        l = 0

        # Initialize the variable to store the length of the longest substring
        res = 0

        # Iterate through the string using the right pointer
        for r in range(len(s)):
            # If the current character is already in the set, remove the leftmost character
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # Add the current character to the set
            charSet.add(s[r])

            # Update the length of the longest substring
            res = max(res, r - l + 1)

        # Return the length of the longest substring without repeating characters
        return res
