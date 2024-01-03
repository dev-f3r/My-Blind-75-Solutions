class Solution:

    # Define a class Solution
    class Solution:
        # Define a method isPalindrome that takes a string s as input and returns a boolean value
        def isPalindrome(self, s: str) -> bool:
            # Convert the string to lowercase
            b = s.lower()
            # Initialize two pointers, l and r, pointing to the start and end of the string respectively
            l = 0
            r = len(b) - 1
            # Iterate until the pointers meet or cross each other
            while l < r:
                # If the character at the left pointer is not alphanumeric, move the left pointer to the right
                if not b[l].isalnum():
                    l += 1
                # If the character at the right pointer is not alphanumeric, move the right pointer to the left
                if not b[r].isalnum():
                    r -= 1
                # If both characters at the left and right pointers are alphanumeric
                if b[r].isalnum() and b[l].isalnum():
                    # If the characters are not equal, the string is not a palindrome, return False
                    if b[l] != b[r]:
                        return False
                    # Move the pointers towards each other
                    r -= 1
                    l += 1
            # If the loop completes without returning False, the string is a palindrome, return True
            return True