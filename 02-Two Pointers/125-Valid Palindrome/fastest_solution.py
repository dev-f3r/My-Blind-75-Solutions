class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase
        s = s.lower()

        # Initialize two pointers, l and r, pointing to the start and end of the string
        l = 0
        r = len(s) - 1

        # Iterate until the pointers meet in the middle
        while l < r:
            # Move the left pointer to the right until it points to an alphanumeric character
            while l < r and not s[l].isalnum():
                l += 1

            # Move the right pointer to the left until it points to an alphanumeric character
            while l < r and not s[r].isalnum():
                r -= 1

            # If the characters at the left and right pointers are not equal, the string is not a palindrome
            if s[l] != s[r]:
                return False
            else:
                # Move the pointers towards the middle
                l += 1
                r -= 1

        # If the loop completes without returning False, the string is a palindrome
        return True
