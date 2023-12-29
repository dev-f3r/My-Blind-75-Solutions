from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to store the counts of each unique number
        counts = dict()

        # Iterate through each number in the input list
        for n in nums:
            # Increment the count for the current number, or initialize to 1 if not present
            counts[n] = 1 + counts.get(n, 0)

        # Sort the unique numbers based on their counts in descending order
        # and return the top k elements
        return sorted(counts.keys(), key=lambda x: counts[x], reverse=True)[:k]
