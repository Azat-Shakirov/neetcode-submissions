class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setn = set(nums)
        streak = 0
        for num in setn:
            if num - 1 not in setn:
                newstreak = 1
                while num + newstreak in setn:
                    newstreak += 1
                streak = max(streak, newstreak)
        return streak