class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li = []
        for arr in matrix:
            li.extend(arr)
        
        l, r = 0, len(li) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if li[m] < target:
                l = m + 1
            elif li[m] > target:
                r = m - 1
            else:
                return True
        return False
