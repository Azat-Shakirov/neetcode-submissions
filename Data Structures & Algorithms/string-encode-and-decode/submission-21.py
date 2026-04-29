class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        li = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            li.append(s[j+1:j+1+num])
            i = j + 1 + num
        return li