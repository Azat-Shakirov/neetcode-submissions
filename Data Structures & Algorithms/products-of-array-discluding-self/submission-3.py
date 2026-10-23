class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # add every product to array
        # no division
        # 1 loop through nums
        output = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        for i in reversed(range(len(nums))):
            output[i] *= suffix
            suffix *= nums[i]
        return output