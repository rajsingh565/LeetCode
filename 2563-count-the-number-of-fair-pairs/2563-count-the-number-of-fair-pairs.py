class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1
        ans = math.comb(n,2)
        #check for pair sum less than lower 
        while left < right : 
            val = nums[left] + nums[right]
            if val < lower : 
                ans -= (right-left)
                left += 1
            else:
                right -= 1
        #check for pair sum more than upper
        left = 0 
        right = n - 1
        while left < right : 
            val = nums[left] + nums[right]
            if val > upper : 
                ans -= (right-left)
                right -= 1
            else:
                left += 1
        return ans 