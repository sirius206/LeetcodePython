# 1. Two pointer 1, Time O(N^2) Space: O(n) or O(logn) depending on sorting 

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for i in range(len(nums)):
            res = self.twoSumII(nums, res, target, i)
            if res == target:
                return res
        return res    
            
    def twoSumII(self, nums, res, target, i):
        lo = i + 1
        hi = len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if abs(target - sum) < abs(target - res):
                res = sum
            
            if target > sum:
                lo += 1
            elif target < sum:
                hi -= 1
            else:
                return res
        return res             
        
# 2. Two pointer 2,         
 class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff       
      
 # 3 binary search O(n^2 logn)     
