class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 = {}
        for i, num in enumerate(nums):
            if num not in dict1:
                dict1[num] = num
            else:
                del dict1[num]
        fkey = next(iter(dict1))
        return dict1[fkey]