#1. use array to count then update all
class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        if n == 1:
            return res
        for i in range(2, n + 1):
            count = []
            order = []
            newres = ""
            for j in range(len(res)):
                if j == 0 or res[j] != res[j - 1]:
                    order.append(int(res[j]))
                    count.append(0)
                count[len(order) - 1] += 1
            for k in range(len(order)):
                newres = newres + str(count[k]) + str(order[k])
            res = newres
        return res
        
#2. or update res every time
class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        if n == 1:
            return res
        for i in range(2, n + 1):
            newres = ""
            j = 0
            while j < len(res):
                num = res[j]
                count = 1
                while j + 1 < len(res) and res[j + 1] == res[j]:
                    count += 1
                    j += 1
                newres = newres + str(count) + num
                j += 1
            res = newres
        return res
