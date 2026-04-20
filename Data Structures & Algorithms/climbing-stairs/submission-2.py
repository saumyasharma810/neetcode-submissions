class Solution:
    ans = {}
    def climbStairs(self, n: int) -> int:
        if n in self.ans:
            return self.ans[n]
        if n < 0:
            return 0
        if n == 0:
            return 1
        self.ans[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.ans[n]
        