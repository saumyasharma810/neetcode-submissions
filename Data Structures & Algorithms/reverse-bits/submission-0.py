class Solution:
    def reverseBits(self, n: int) -> int:
        power = 31
        ans = 0
        while n:
            if n%2 == 1:
                ans += 2**power
            n//=2
            power-=1
        return ans

        