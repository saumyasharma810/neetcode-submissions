class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [float("inf")] * (len(cost)+2)
        min_cost[0] = 0
        min_cost[1] = 0
        for i in range(len(cost)):
            min_cost[i+1] = min(min_cost[i+1], min_cost[i]+cost[i])
            min_cost[i+2] = min(min_cost[i+2], min_cost[i]+cost[i])
        return min_cost[len(cost)]

        