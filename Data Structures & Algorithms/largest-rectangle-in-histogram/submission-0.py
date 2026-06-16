class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        for i in range(n):
            min_height = heights[i]
            for j in range(i,n):
                min_height = min(min_height, heights[j])
                ans = max(ans, min_height * ((j-i)+1))
        return ans


        