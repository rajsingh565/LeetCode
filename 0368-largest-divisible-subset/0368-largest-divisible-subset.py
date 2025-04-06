class Solution:

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        prev=[[] for i in range(n+1)]
        for i in range(1,n+1):
            curr=[[] for i in range(n+1)]
            for j in range(1,n+1):
                x=[]
                if (j-1)==0 or (nums[j-1]%nums[i-1]==0 or nums[i-1]%nums[j-1]==0):
                    x=prev[i]+[nums[i-1]]
                y=prev[j]
                if len(y)>len(x):
                    curr[j]=y[:]
                else:
                    curr[j]=x[:]
            prev=curr[:]
        return prev[1]
