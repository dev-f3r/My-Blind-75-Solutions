class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)  # Create a set of unique numbers from the input list
        longest = 0  # Initialize the variable to store the length of the longest consecutive sequence

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:  # If the previous number is not in the set, it means n is the start of a sequence
                length = 0  # Initialize the length of the current sequence
                while (n + length) in numSet:  # Check if the next number is in the set, indicating the sequence continues
                    length += 1  # Increment the length of the current sequence

                longest = max(longest, length)  # Update the longest length if necessary
        
        return longest  # Return the length of the longest consecutive sequence