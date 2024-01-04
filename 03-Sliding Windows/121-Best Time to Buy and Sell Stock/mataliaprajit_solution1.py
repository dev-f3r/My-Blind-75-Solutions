class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price and maximum profit variables
        min_price = prices[0]
        max_profit = 0

        # Iterate through the prices starting from the second element
        for price in prices[1:]:
            # Update the maximum profit by comparing the current profit with the stored maximum
            max_profit = max(max_profit, price - min_price)

            # Update the minimum price if the current price is smaller
            min_price = min(min_price, price)

        # Return the maximum profit obtained
        return max_profit
