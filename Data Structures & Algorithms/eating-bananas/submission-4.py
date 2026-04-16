class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, sum(piles)
        res = r
        while l<=r:
            mid = l + (r-l)//2
            hours = 0
            for pile in piles:
                hours += pile//mid if pile%mid == 0 else (pile//mid) + 1
            if hours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid+1
        return res
