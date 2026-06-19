class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = x
        mul = True
        if n == 0:
            return 1
        if n < 0:
            mul = False
        n-=1
        n = abs(n)
        while n:
            ans = ans * x if mul else ans / x
            n-=1
        return ans
        