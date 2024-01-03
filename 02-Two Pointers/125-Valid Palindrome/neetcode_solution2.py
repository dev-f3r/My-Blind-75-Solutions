class Solution:

    class Solution:
        def isPalindrome(self, s: str) -> bool:
            # Initialize two pointers, l and r, pointing to the start and end of the string
            l, r = 0, len(s) - 1

            while l < r:
                # Move l pointer to the right until it reaches an alphanumeric character
                while l < r and not self.alphaNum(s[l]):
                    l += 1

                # Move r pointer to the left until it reaches an alphanumeric character
                while l < r and not self.alphaNum(s[r]):
                    r -= 1

                # Check if the characters at l and r are equal (ignoring case)
                if s[l].lower() != s[r].lower():
                    return False

                # Move l pointer to the right and r pointer to the left
                l, r = l + 1, r - 1

            # If the loop completes without returning False, the string is a valid palindrome
            return True

        def alphaNum(self, c: str) -> bool:
            # Check if the character is alphanumeric
            return (
                ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
            )