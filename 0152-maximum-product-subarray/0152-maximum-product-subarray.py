class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curr=1
        maxProduct1=max(nums)

        for i in range(len(nums)):
            if nums[i]==0:
                curr=1
                continue

            curr*=nums[i]
            maxProduct1=max(maxProduct1,curr)

        
        curr=1
        maxProduct2=max(nums)

        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                curr=1
                continue

            curr*=nums[i]
            maxProduct2=max(maxProduct2,curr)

        return max(maxProduct1,maxProduct2)