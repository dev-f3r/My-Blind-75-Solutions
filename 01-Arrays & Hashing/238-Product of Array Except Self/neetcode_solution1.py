from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize a result list with all elements set to 1
        res = [1] * len(nums)

        # Calculate the product of all elements to the left of each index
        prefix_product = 1
        for i in range(len(nums)):
            # Store the product of all elements to the left (prefix) in the result list
            res[i] = prefix_product
            # Update the prefix product for the next iteration
            prefix_product *= nums[i]

        # Calculate the product of all elements to the right of each index
        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the existing result by the product of all elements to the right (postfix)
            res[i] *= postfix_product
            # Update the postfix product for the next iteration
            postfix_product *= nums[i]

        # Return the final result list containing the product of all elements except the one at each index
        return res
