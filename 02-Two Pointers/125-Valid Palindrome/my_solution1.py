# Leetcode: 125. Valid Palindrome
class Solution:
    """Class to check if a string is a valid palindrome."""

    def isPalindrome(self, s: str) -> bool:
        """Check if the given string is a valid palindrome.

        Args:
            s (str): The input string.

        Returns:
            bool: True if the string is a valid palindrome, False otherwise.
        """
        if s == "":
            return True

        formatted_s = self.format(s)

        # Use two pointers to compare characters from both ends of the string
        for i in range(len(formatted_s) // 2):
            if formatted_s[i] != formatted_s[len(formatted_s) - 1 - i]:
                return False

        return True

    def format(self, s: str) -> str:
        """Format the string by removing non-alphanumeric characters and converting to lowercase.

        Args:
            s (str): The input string.

        Returns:
            str: The formatted string.
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        out = ""
        for letter in s.lower():
            if letter in alphabet or letter.isdigit():
                out += letter

        return out


# Make some test cases
s = Solution()

# Test case 1: Empty string
assert s.isPalindrome("") == True

# Test case 2: Single character
assert s.isPalindrome("a") == True

# Test case 3: Palindrome with only alphanumeric characters
assert s.isPalindrome("A man, a plan, a canal: Panama") == True

# Test case 4: Non-palindrome with only alphanumeric characters
assert s.isPalindrome("race a car") == False

# Test case 5: Palindrome with alphanumeric and non-alphanumeric characters
assert s.isPalindrome("Able , was I saw eLba") == True

# Test case 6: Non-palindrome with alphanumeric and non-alphanumeric characters
assert s.isPalindrome("Hello, World!") == False

print("All test cases passed!")
