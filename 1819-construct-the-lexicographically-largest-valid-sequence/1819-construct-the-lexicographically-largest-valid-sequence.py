from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        a = [0] * (2 * n - 1)
        b = [False] * (n + 1)
        
        def c(d: int) -> bool:
            if d == len(a):
                return True
            
            if a[d] != 0:
                return c(d + 1)
            
            for e in range(n, 0, -1):
                if b[e]:
                    continue
                if e == 1:
                    a[d] = 1
                    b[1] = True
                    if c(d + 1):
                        return True
                    a[d] = 0
                    b[1] = False
                else:
                    f = d + e
                    if f < len(a) and a[f] == 0:
                        a[d], a[f] = e, e
                        b[e] = True
                        if c(d + 1):
                            return True
                        a[d], a[f] = 0, 0
                        b[e] = False
            
            return False
        
        c(0)
        return a