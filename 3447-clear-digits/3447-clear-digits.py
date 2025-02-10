class Solution:
    def clearDigits(self, s: str) -> str:
        x = []
        for i in s:
            if i.isdigit():
                if x:
                    x.pop()
            else:
                x.append(i)
        return "".join(x)