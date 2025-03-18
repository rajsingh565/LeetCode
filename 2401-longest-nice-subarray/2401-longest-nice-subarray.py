class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_length, left, used_bits = 1, 0, 0
        for right in range(len(nums)):
            while used_bits & nums[right]:
                used_bits ^= nums[left]
                left += 1
            used_bits |= nums[right]
            max_length = max(max_length, right - left + 1)
        return max_length