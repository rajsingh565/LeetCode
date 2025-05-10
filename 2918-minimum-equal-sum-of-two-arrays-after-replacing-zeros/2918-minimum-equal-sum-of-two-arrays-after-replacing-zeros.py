class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(n if n != 0 else 1 for n in nums1)
        sum2 = sum(n if n != 0 else 1 for n in nums2)

        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)

        if (zeros1 == 0 and sum2 > sum1) or (zeros2 == 0 and sum1 > sum2):
            return -1

        return max(sum1, sum2)
        