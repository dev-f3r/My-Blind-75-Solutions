from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store the count of each number in the input list
        count = {}

        # List of lists to store numbers grouped by frequency (index represents frequency)
        freq = [[] for _ in range(len(nums) + 1)]

        # Count the occurrences of each number in the input list
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Group numbers by their frequency
        for n, c in count.items():
            freq[c].append(n)

        # Result list to store the top k frequent numbers
        res = []

        # Iterate through the frequency lists in reverse order
        for i in range(len(freq) - 1, 0, -1):
            # Iterate through numbers in the current frequency list
            for n in freq[i]:
                # Append the number to the result list
                res.append(n)
                # Check if the result list has reached the desired size (k)
                if len(res) == k:
                    # Return the result list when k elements are found
                    return res

        # Return an empty list if there are not enough elements to satisfy k
        return []
