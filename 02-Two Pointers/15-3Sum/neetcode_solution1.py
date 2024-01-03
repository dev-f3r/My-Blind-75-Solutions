from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the input list in ascending order

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:  # Skip duplicate elements
                continue

            l, r = i + 1, len(nums) - 1  # Set left and right pointers

            while l < r:
                threeSum = a + nums[l] + nums[r]  # Calculate the sum of three elements

                if threeSum > 0:  # If the sum is greater than 0, move the right pointer to the left
                    r -= 1
                elif threeSum < 0:  # If the sum is less than 0, move the left pointer to the right
                    l += 1
                else:  # If the sum is equal to 0, add the triplet to the result list
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    # Skip duplicate elements
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
