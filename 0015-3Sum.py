#1. Better. Two pinters Time Complexity: O(n^2), twoSumII is O(n), and we call it n times. 
# Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm      
class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()
        for i in range(len(nums)):
# don't need to check the other half since array is sorted
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            self.twoSumII(nums, i, res)
        return res    
        
    def twoSumII(self, nums: List[int], i:int, res: List[List[int]]) -> None:
        lo = i + 1
        hi = len(nums) - 1
        while (lo < hi):
            sum = nums[lo] + nums[hi] + nums[i]
            if sum == 0:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while (lo < hi) and nums[lo] == nums[lo - 1]:
                    lo += 1
            elif sum > 0:
                hi -= 1
            else:
                lo += 1   
      
# 2. Mine, HashMap Time O(n^2) Space O(n)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hm = {}
        nums.sort()
        res = []
        for i in range(len(nums)):
            hm[nums[i]] = i
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j >= i + 2 and nums[j] == nums[j - 1]:
                    continue
                sum2 = (nums[i] + nums[j]) * (-1)
                if sum2 < 0:
                    break
                if sum2 >= nums[j] and sum2 in hm.keys() and i != hm.get(sum2) and j != hm.get(sum2):
                    res.append([nums[i], nums[j], sum2])
        
        return res
                    
                    
# 3 No sort  Time Complexity: O(n^2)  Space O(n) for the hashmap       
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res                    
