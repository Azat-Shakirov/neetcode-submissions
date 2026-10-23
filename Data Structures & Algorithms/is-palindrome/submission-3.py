class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for c in s:
            if c.isalnum():
                s1 = s1 + c
        s1rev = "".join(reversed(s1))
        return s1.lower() == s1rev.lower()