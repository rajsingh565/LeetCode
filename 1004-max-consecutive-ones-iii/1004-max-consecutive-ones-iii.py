class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left=0
        count=0
        ln=0
        for right in range(n):
            if nums[right]==0:
                count+=1
            if count>k:
                if nums[left]==0:
                    count-=1
                left+=1
            if count<=k:
                ln=max(ln,right-left+1)
        return ln
        