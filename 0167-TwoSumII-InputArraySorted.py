# method 2: two pointers
# Time: O(N) space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        while (lo < hi):
            if target == numbers[lo] + numbers[hi]:
                return [lo+1, hi+1]
            elif target < numbers[lo] + numbers[hi]:
                hi -= 1
            else:
                lo += 1
        return [-1, -1]        
