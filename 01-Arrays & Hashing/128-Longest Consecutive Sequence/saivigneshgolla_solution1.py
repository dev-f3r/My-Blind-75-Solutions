from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set to store the unique numbers from the input list
        numSet = set(nums)
        # Initialize the maximum sequence length to 0
        maxSeqLen = 0
        # Iterate until the maximum sequence length is less than the size of the set
        while maxSeqLen < len(numSet):
            # Pop a number from the set
            num = numSet.pop()
            # Find the longest consecutive sequence starting from the popped number
            longest = num + 1
            while longest in numSet:
                numSet.remove(longest)
                longest += 1
            # Find the longest consecutive sequence ending at the popped number
            num = num - 1
            while num in numSet:
                numSet.remove(num)
                num -= 1
            # Update the maximum sequence length if necessary
            maxSeqLen = max(maxSeqLen, longest - num - 1)
        # Return the maximum sequence length
        return maxSeqLen


# make some test cases
solution = Solution()
# print(
#     solution.longestConsecutive([100, 4, 200, 1, 3, 2])
# )  # 4 sequence_0 = [1, 2, 3, 4]
# print(solution.longestConsecutive([1, 2, 3, 4, 6, 7, 8, 12, 13, 14, 15, 16]))  # 5
print(solution.longestConsecutive([5, 4, 3, 2, 1]))  # 3