from typing import List
import pdb


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the maximum profit variable
        res = 0

        # Initialize pointers for buying (l) and selling (r)
        l, r = 0, 1

        # Iterate through the prices array
        while r < len(prices):
            # Set a breakpoint for debugging
            pdb.set_trace()

            # Calculate the profit between the current buying and selling points
            profit = prices[r] - prices[l]

            # Update the maximum profit if the current profit is greater
            res = max(res, profit)

            # If the current profit is less than or equal to 0, update the buying point
            if profit <= 0:
                l = r
                r += 1
            else:
                # Move to the next selling point
                r += 1

        # Return the maximum profit obtained
        return res


# Create an instance of the Solution class
s = Solution()

# Test cases
assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert s.maxProfit([7, 6, 4, 3, 1]) == 0
assert s.maxProfit([1, 2]) == 1
