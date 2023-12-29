class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, el in enumerate(nums):
            hashmap[el] = i
        
        for i, el in enumerate(nums):
            diff = target - el
            if diff in hashmap and hashmap[diff] != i:
                return [i, hashmap[diff]]

        return [-1]


solution1 = Solution()
print(solution1.twoSum([2,7,11,15], 9)) # 0,1
print('------------------------------')
print(solution1.twoSum([3,2,4], 6)) # 1,2
print('------------------------------')
print(solution1.twoSum([3,3], 6)) # 0,1
print('------------------------------')
print(solution1.twoSum([2,5,5,11], 10)) # 1,2
