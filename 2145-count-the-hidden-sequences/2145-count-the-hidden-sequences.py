class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        cur=0
        hi=0
        lo=0
        for i in diff:
            cur+=i
            hi=max(hi,cur)
            lo=min(lo,cur)
            if hi-lo>upper-lower:
                return 0
        return (upper-lower)-(hi-lo)+1