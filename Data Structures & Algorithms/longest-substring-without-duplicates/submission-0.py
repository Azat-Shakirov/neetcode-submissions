class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # window of unique char
        # when a duplicate appears -> update the left side of the window
        # we can use dict for O(1) look up
        l = 0
        res = 0
        charset = set()

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r - l + 1)
        return res