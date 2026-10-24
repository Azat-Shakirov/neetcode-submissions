class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxnum = 0
        l, r = 0, len(heights) - 1
        while l < r:
            if heights[l] > heights[r]:
                water = (r - l) * heights[r]
                r -= 1
            else:
                water = heights[l] * (r - l)
                l += 1
            if water > maxnum:
                maxnum = water
        return maxnum