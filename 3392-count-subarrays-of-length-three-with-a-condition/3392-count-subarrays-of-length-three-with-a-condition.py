class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        cnt=0
        left=0
        right=2
        n=len(nums)
        while right<n:
            if (nums[left]+nums[right])*2==nums[left+1]:
                cnt+=1
            left+=1
            right+=1
        return cnt