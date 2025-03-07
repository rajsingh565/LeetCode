class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sev = [1]*(right+1)
        sev[0],sev[1] = 0,0
        for i in range(2,right+1):
            if sev[i]==1:
                temp = i+i
                while temp<right+1:
                    sev[temp]=0
                    temp+=i
        res = []
        for i in range(left,right+1):
            if sev[i]==1:
                res.append(i)
        if len(res)<2:
            return [-1,-1]
        i = 0
        j = i+1
        diff = float('inf')
        ans = []
        while j<len(res):
            if res[j]-res[i]<diff:
                ans = [res[i],res[j]]
                diff = res[j]-res[i]
            i+=1
            j+=1
        return ans