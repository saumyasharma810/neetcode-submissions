class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for start in range(n):
            tg = 0
            for i in range(start, start+n):
                tg += gas[i%n]
                tg-=cost[i%n]
                if tg < 0:
                    break
            if tg >= 0:
                return start
        return -1