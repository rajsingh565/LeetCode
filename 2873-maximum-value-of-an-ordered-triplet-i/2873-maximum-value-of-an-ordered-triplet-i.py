class Solution:
    def maximumTripletValue(self, nums):
        n = len(nums)
        maxTriplet = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    value = (nums[i] - nums[j]) * nums[k]
                    maxTriplet = max(maxTriplet, value)
        
        return maxTriplet