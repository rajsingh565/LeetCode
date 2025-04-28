class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l=0
        ans=0
        s=0
        a=0
        for r in range(len(nums)):
            s+=nums[r]
            a=s*(r-l+1)
            while a>=k:
                s-=nums[l]
                l+=1
                a=s*(r-l+1)
                #l+=1
            ans+=(r-l+1)
        return ans