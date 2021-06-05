#1. answer, use str function
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # formats range in the requested format
        def formatRange(lower, upper):
            if lower == upper:
                return str(lower)
            return str(lower) + "->" + str(upper)

        result = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= curr - 1:
                result.append(formatRange(prev + 1, curr - 1))
            prev = curr
        return result

#2. mine
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def formatstring(lo, hi):
            if lo == hi:
                return str(lo)
            else:
                return str(lo) + "->" + str(hi)             
        res = []
        
        if len(nums) == 0:
            lo = lower
            hi = upper
            res.append(formatstring(lo, hi))        
            return res
        
        
        if nums[0] != lower:
            lo = lower
            hi = nums[0] - 1
            res.append(formatstring(lo, hi))  
            
        i = 0    
        while i < len(nums) - 1:
            if nums[i + 1] > nums[i] + 1:
                lo = nums[i] + 1
                hi = nums[i + 1] - 1
                res.append(formatstring(lo, hi))  
            i += 1       
            
        if i == len(nums) - 1 and nums[i] != upper:
            lo = nums[i] + 1
            hi = upper
            res.append(formatstring(lo, hi))  
            
        return res   
