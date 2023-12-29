class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            # if the solution is found, returns the solution
            if diff in prevMap:
                return [prevMap[diff], i]

            # if the solution is not found, update the hashmap
            prevMap[n] = i

        return [-1,-1]


solution1 = Solution()
print(solution1.twoSum([2,7,11,15], 9)) # 0,1
print('------------------------------')
print(solution1.twoSum([3,2,4], 6)) # 1,2
print('------------------------------')
print(solution1.twoSum([3,3], 6)) # 0,1
print('------------------------------')
print(solution1.twoSum([2,5,5,11], 10)) # 1,2
