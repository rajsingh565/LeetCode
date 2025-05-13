class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod=10**9+7
        temp=[0]*26
        for ch in s:
            temp[ord(ch)-ord('a')]+=1

        while t>0:
            p=[0]*26
            for i in range(26):
                if i ==25:
                    p[0]+=temp[i]
                    p[1]+=temp[i]
                else:
                    p[i+1]+=temp[i]
                p[i] %= mod
            temp=p
            t-=1 

        return sum(temp)%mod
                           