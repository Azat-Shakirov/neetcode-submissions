class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        count = {}
        for num in nums:
            if num - 1 not in set1:
                length = 1
                while num + length in set1:
                    length += 1
                count[num] = length
        return max(count.values(), default=0)