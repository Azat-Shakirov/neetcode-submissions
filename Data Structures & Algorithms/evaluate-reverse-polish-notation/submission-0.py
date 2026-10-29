class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        li = []
        for c in tokens:
            if c == "+":
                li.append(li.pop() + li.pop())
            elif c == "-":
                a, b = li.pop(), li.pop()
                li.append(b - a)
            elif c == "*":
                li.append(li.pop() * li.pop())
            elif c == "/":
                a, b = li.pop(), li.pop()
                li.append(int(float(b) / a))
            else:
                li.append(int(c))
        return li[0]