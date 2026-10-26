class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for num in nums:
            if res != num:
                return res
            else:
                res += 1
        return res