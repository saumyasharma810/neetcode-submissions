class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, sum(piles)
        while l<r:
            mid = l + (r-l)//2
            hours = 0
            for pile in piles:
                hours += pile//mid if pile%mid == 0 else (pile//mid) + 1
            if hours <= h:
                r = mid
            else:
                l = mid+1
        hours = 0
        for pile in piles:
            hours += pile//l if pile%l == 0 else (pile//l) + 1
        return l if hours<=l else r
