class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        water_trapped = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom = height[stack.pop()]
                if stack:
                    left_ind = stack[-1]
                    left_h = height[left_ind]
                    h = min(left_h, height[i])-bottom
                    d = i-left_ind-1
                    water_trapped += max(0,h*d)
            stack.append(i)
        return water_trapped


        