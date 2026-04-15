class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        for i in range(len(heights)-1):
            for j in range(1,len(heights)):
                water = max(water, (j-i)*min(heights[i],heights[j]))
        return water

        
        
        