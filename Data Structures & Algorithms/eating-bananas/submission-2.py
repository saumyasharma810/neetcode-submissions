class Solution:

    def canBeDone(self, x: int, h: int, piles: List[int]) -> bool:
        hours = 0
        for pile in piles:
            hours += pile//x if pile%x == 0 else (pile//x) + 1
        return True if hours <= h else False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, sum(piles)
        while l<r:
            mid = l + (r-l)//2
            if self.canBeDone(mid,h,piles):
                r = mid
            else:
                l = mid+1
        return l if self.canBeDone(l,h,piles) else r
