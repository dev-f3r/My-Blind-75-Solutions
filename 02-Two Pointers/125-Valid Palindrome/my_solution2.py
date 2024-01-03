import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determines whether a given string is a valid palindrome.

        Args:
            s (str): The input string to check.

        Returns:
            bool: True if the string is a valid palindrome, False otherwise.
        """
        # Remove non-alphanumeric characters and convert to lowercase
        s = re.findall('[a-zA-Z0-9]', s.lower())

        # Check if the string is a palindrome
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False

        return True


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
