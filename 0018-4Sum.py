Two pointers Time: O(n^3), Space: O(1)?
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, len(nums)):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        lo = j + 1
                        hi = len(nums) - 1
                        while (lo < hi):
                            sum = nums[i] + nums[j] + nums[lo] + nums[hi]
                            if sum < target:
                                lo += 1
                            elif sum > target:
                                hi -= 1
                            else:
                                res.append([nums[i], nums[j], nums[lo], nums[hi]])
                                lo += 1
                                hi -= 1
                                while lo < hi and nums[lo] == nums[lo - 1]:
                                    lo += 1
        return res
        
#2. Recursive two pointers, faster Time: O(n^3), Space: O(n)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1
            while (lo < hi):
                sum = nums[lo] + nums[hi]
                if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
