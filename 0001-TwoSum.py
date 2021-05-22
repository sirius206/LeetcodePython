// 2 for loops
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(n):
            d[target - nums[i]] = i
        for i in range(n):
            if nums[i] in d.keys() and i !=d[nums[i]]:
                return[i, d[nums[i]]]
                
// 1 for loop
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(n):
            if nums[i] in d.keys() and i !=d[nums[i]]:
                return[i, d[nums[i]]]
            d[target - nums[i]] = i                
