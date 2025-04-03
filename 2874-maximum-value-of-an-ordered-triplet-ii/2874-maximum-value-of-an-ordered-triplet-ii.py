from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        
        self.prefix_max(prefix, nums)
        self.suffix_max(suffix, nums)
        
        ans = 0
        for j in range(1, n - 1):
            ans = max(ans, (prefix[j - 1] - nums[j]) * suffix[j + 1])
        
        return ans

    def prefix_max(self, prefix: List[int], nums: List[int]) -> None:
        max_val = prefix[0] = nums[0]
        for i in range(1, len(nums)):
            max_val = max(max_val, nums[i])
            prefix[i] = max_val

    def suffix_max(self, suffix: List[int], nums: List[int]) -> None:
        max_val = suffix[len(nums) - 1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            max_val = max(max_val, nums[i])
            suffix[i] = max_val