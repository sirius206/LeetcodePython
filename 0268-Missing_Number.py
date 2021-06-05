# 1. difference of sum, Time O(n), Space O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_n = len(nums) * (len(nums) + 1) / 2
        sum_nums = 0 
        for i in range(len(nums)):
            sum_nums += nums[i]
        return int(sum_n - sum_nums)

# 2 hashset
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

# 3. XOR
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

