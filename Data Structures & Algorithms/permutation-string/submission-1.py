class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = ''.join(sorted(s1))
        for l in range(len(s2)):
            sub = ''.join(sorted(s2[l:l+n]))
            if sub == s1:
                return True
        return False