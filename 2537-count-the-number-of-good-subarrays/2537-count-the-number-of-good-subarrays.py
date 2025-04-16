class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        ans = 0
        numPairs = 0
        l = 0
        r = 0
        counts = {}

        while r < len(nums):
            numPairs += counts.get(nums[r], 0)
            counts[nums[r]] = counts.get(nums[r], 0) + 1

            while numPairs >= k:
                # We have a good subarray nums[l:r+1]
                # Therefore all subarrays starting at l and
                # ending at r through len(nums) - 1 are good
                ans += len(nums) - r

                counts[nums[l]] -= 1
                numPairs -= counts[nums[l]]
                l += 1
            r += 1
        
        return ans