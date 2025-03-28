class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        long = 0
        count = 0
        for val in nums:
            if val == 1:
                count += 1
                long = max(long, count) 
            else:
                count = 0
        return long