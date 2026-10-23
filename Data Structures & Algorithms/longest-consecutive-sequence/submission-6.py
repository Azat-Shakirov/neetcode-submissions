class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        sortedn = sorted(list(set(nums)))
        streak = 1
        newstreak = 1
        for i in range(len(sortedn)-1):
            if sortedn[i+1] == sortedn[i] + 1:
                newstreak += 1
            else:
                newstreak = 1
            if newstreak > streak:
                streak = newstreak
        return streak