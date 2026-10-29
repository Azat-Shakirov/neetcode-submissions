class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack1 = []
        for i, t in enumerate(temperatures):
            while stack1 and t > temperatures[stack1[-1]]: 
                j = stack1.pop()
                result[j] = i - j
            stack1.append(i)
        return result