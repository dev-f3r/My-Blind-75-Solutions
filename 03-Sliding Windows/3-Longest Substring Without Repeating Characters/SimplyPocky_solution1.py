class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = result = 0  # Initialize start and result variables
        seen = {} # Create an empty dictionary to store seen characters and their indices

        for i, letter in enumerate(s):  # Iterate through the string
            if (
                seen.get(letter, -1) >= start
            ):  # If the current letter is already seen and its index is greater than or equal to the start index
                start = (
                    seen[letter] + 1
                )  # Update the start index to the next index of the repeated letter

            result = max(
                result, i - start + 1
            )  # Calculate the length of the current substring without repeating characters

            seen[
                letter
            ] = i  # Store the index of the current letter in the seen dictionary

        return result  # Return the length of the longest substring without repeating characters


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
