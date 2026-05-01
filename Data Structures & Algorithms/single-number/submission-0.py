class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1
        return min(dict1, key=dict1.get)