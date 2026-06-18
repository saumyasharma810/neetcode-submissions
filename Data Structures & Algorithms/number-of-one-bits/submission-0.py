class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n:
            ones += 1 if n%2==1 else 0
            n//=2
        return ones

        