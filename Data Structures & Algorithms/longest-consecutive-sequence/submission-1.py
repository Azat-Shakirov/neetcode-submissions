class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        longest = 0
        for num in set1:
            if num - 1 not in set1:
                length = 1
                while num + length in set1:
                    length += 1
                longest = max(longest, length)
        return longest