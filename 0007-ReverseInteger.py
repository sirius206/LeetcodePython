class Solution:
    def reverse(self, x: int) -> int:
        digits = []
        if x < 0: 
            neg = True
            x = - x
        else: neg = False    
        res = 0  
        while (x != 0):
            if res < -2**31 / 10 or res > (2**31 -1) / 10:
                return 0
            res = res * 10 + (x % 10)
            x = x // 10

        if neg: res = -res
        return res  
