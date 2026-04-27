class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
        sorted_keys = sorted(count, key=count.get, reverse=True)
        return sorted_keys[:k]