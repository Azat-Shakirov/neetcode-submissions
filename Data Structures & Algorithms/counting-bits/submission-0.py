class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        count = 0
        for i in range(n + 1):
            if i == 0:
                continue
            k = i
            while k:
                count += 1 if k & 1 else 0
                k >>= 1
            res.append(count)
            count = 0
        return res