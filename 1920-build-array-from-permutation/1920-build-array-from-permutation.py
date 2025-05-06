class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            result.append(nums[nums[i]])
        return result