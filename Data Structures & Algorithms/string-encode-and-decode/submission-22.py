class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            charnum = str(len(s))
            result = result + charnum + "." + s
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != ".":
                j += 1
            num = int(s[i:j])
            result.append(s[j+1:j+1+num])
            i = j + 1 + num
        return result

