class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        result = []
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1
        containers = [[] for i in range(len(nums) + 1)]
        for num, freq in dict1.items():
            containers[freq].append(num)
        for container in reversed(containers):
            for num in container:
                result.append(num)
                if len(result) == k:
                    return result