class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        j = 1
        for i, el1 in enumerate(nums):
            for el2 in nums[i+1:]:
                print(f"{i}:{el1}, {j}:{el2}")
                if(el1 + el2 == target):
                    return [i,j]
                else:
                    j += 1

            j = i + 2

        return [-1,-1]



solution1 = Solution()
print(solution1.twoSum([2,7,11,15], 9)) # 0,1
print('------------------------------')
print(solution1.twoSum([3,2,4], 6)) # 1,2
print('------------------------------')
print(solution1.twoSum([3,3], 6)) # 0,1
print('------------------------------')
print(solution1.twoSum([2,5,5,11], 10)) # 1,2
