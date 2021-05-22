class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = {}
        left = 0
        for i in range(n):
            if s[i] in dp:
                left = max(dp[s[i]], left)
                
            res = max(res, i - left + 1)
            dp[s[i]] = i + 1
        return res    
