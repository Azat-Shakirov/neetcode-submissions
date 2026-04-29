class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # 4 - 1,2,4,6
        output = [1] * n # [1,1,1,1]

        prefix = 1 # 1,2,8,48
        for i in range(n): # 0,1,2,3
            output[i] = prefix # [1,1,2,8]
            prefix *= nums[i] # 1*1=1; 1*2=2; 2*4=8; 48

        suffix = 1 # 6
        for i in reversed(range(n)): #(start at 3, stop at -1(last index), step by -1)
            output[i] *= suffix # [8]
            suffix *= nums[i]

        return output