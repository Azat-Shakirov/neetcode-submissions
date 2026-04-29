class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        li1 = []
        for i, num in enumerate(nums):
            prefix = nums[:i]
            suffix = nums[i+1:]
            total = 1
            for n in prefix + suffix:
                total = total * n
            li1.append(total)
        return li1