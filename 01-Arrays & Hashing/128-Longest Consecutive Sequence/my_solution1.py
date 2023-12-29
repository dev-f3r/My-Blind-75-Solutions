# leetcode: 128 - Longest Consecutive Sequence
from typing import List
from collections import defaultdict


from typing import List
from collections import defaultdict

class Solution:
    """
    Class to find the length of the longest consecutive sequence in a list of integers.

    Attributes:
        nums (List[int]): The list of integers.

    Methods:
        longestConsecutive: Finds the length of the longest consecutive sequence.
    """

    def longestConsecutive(self, nums: List[int]) -> int:
            """
            Finds the length of the longest consecutive sequence in a list of integers.

            Args:
                nums (List[int]): The list of integers.

            Returns:
                int: The length of the longest consecutive sequence.
            """
            # Create a set of unique numbers from the input list
            s_nums = set(nums)

            # Create a dictionary to store sequences
            sequences = defaultdict(list)
            j = 0
            for curr in s_nums:
                key = f"seq_{j}"
                # If the current number minus 1 is not in the set, it means it is the start of a new sequence
                if curr - 1 not in s_nums:
                    sequences[key].append(curr)
                    # Continue adding consecutive numbers to the sequence until there are no more consecutive numbers
                    while curr + 1 in s_nums:
                        curr += 1
                        sequences[key].append(curr)
                    j += 1

            # Return the length of the longest sequence
            return max(len(seq) for seq in sequences.values())


# Make some test cases
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4 sequence_0 = [1, 2, 3, 4] 
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9 sequence_0 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(solution.longestConsecutive([1, 2, 0, 1]))  # 3 sequence_0 = [0, 1, 2]
print(solution.longestConsecutive([1, 2, 0, 1, 2]))  # 3 sequence_0 = [0, 1, 2]
print(solution.longestConsecutive([1, 2, 0, 1, 2, 3]))  # 4 sequence_0 = [0, 1, 2, 3]
print(solution.longestConsecutive([1, 2, 0, 1, 2, 3, 4]))  # 5 sequence_0 = [0, 1, 2, 3, 4]