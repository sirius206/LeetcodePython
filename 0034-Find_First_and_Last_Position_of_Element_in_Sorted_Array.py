# 分开找start， end 分别用binary search Time: O(log n) Space: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        lo = 0
        hi = len(nums) - 1
        while (lo <= hi):
            mid = lo + (hi - lo) // 2
            if nums[mid] == target: 
                if mid == 0 or nums[mid - 1] != target:
                    start = mid
                    break
                else:
                    hi = mid - 1
                    
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
                
        lo = max(0, start)
        hi = len(nums) - 1
        while (lo <= hi):
            mid = lo + (hi - lo) // 2
            if nums[mid] == target: 
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    end = mid
                    break
                else:
                    lo = mid + 1
                    
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
        
        return [start, end]        
