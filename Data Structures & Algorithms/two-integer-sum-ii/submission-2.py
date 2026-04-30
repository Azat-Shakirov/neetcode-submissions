class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        setNum = set(numbers)
        for i, num in enumerate(numbers):
            if target - num in setNum:
                return [i + 1, numbers.index(target - num) + 1]