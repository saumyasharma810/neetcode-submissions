class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = ""
        n,m = len(num1), len(num2)
        i = 0
        a = 0
        while i < n:
            a = a*10 + (ord(num1[i])-ord('0'))
            i+=1
        i = 0
        b = 0
        while i < m:
            b = b*10 + (ord(num2[i])-ord('0'))
            i+=1
        c = a*b
        if c == 0:
            return "0"
        # print(c)
        while c:
            ans += f"{c%10}"
            c//=10
        return ans[::-1]


        
        