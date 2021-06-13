//1. Two pointers Time: O(n^2), Space: O(1)

class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        Arrays.sort(nums);
        int len = nums.length;
        int count = 0;
        for (int i = 0; i < len; i++){
            int lo = i + 1;
            int hi = len - 1;
            while (lo < hi){
                int sum = nums[i] + nums[lo] + nums[hi];
                if (sum < target){
                    count += hi - lo;
                    lo++;
                }
                else if (sum >= target){
                    hi--;
                }
            }
            
        }
        return count;
    }
}

//2 Binary search Time: O(n ^2 logn), Space: O(1)?
public int threeSumSmaller(int[] nums, int target) {
    Arrays.sort(nums);
    int sum = 0;
    for (int i = 0; i < nums.length - 2; i++) {
        sum += twoSumSmaller(nums, i + 1, target - nums[i]);
    }
    return sum;
}

private int twoSumSmaller(int[] nums, int startIndex, int target) {
    int sum = 0;
    for (int i = startIndex; i < nums.length - 1; i++) {
        int j = binarySearch(nums, i, target - nums[i]);
        sum += j - i;
    }
    return sum;
}

private int binarySearch(int[] nums, int startIndex, int target) {
    int left = startIndex;
    int right = nums.length - 1;
    while (left < right) {
        int mid = (left + right + 1) / 2;
        if (nums[mid] < target) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    return left;
