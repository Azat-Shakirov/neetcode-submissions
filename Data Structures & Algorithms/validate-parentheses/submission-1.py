class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        lastc = ""
        for c in s:
            if c == lastc:
                li.pop()
                if not li:
                    lastc = ""
                else:
                    lastc = li[-1]
                continue
            if c == '(':
                lastc = ")"
            elif c == '{':
                lastc = '}'
            elif c == '[':
                lastc = ']'
            else:
                return False
            li.append(lastc)
        return not li