class Solution:
    def trap(self, height: List[int]) -> int:

        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        for i in range(1,len(height)):
            leftMax[i] = max(leftMax[i-1], height[i-1])

        for i in range(len(height)-2,-1,-1):
            rightMax[i] = max(rightMax[i+1], height[i+1])

        water_trapped = 0
        for i in range(len(height)):
            water_trapped += max(0,min(leftMax[i],rightMax[i])-height[i])
    
        return water_trapped


        