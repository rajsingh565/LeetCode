class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = -99999
        Sum = 0
        while (r < len(nums)):
            while (Sum < 0):
                Sum -= nums[l]
                l+=1
            
            Sum += nums[r]
            res = max(res, Sum)
            r+=1
        
        return res