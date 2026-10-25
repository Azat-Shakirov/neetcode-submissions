class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        cnt = 0
        lmax, rmax = height[l], height[r]
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                cnt += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                cnt += rmax - height[r]
        return cnt