class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if (n <= 1): return s 
        dp = [[False] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = True
        start = 0
        maxLen = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if (j - i + 1) > maxLen:
                            maxLen = j - i + 1
                            start = i
        return s[start: start + maxLen]    
