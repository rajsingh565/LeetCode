class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            digits = 0
            while num:
                digits += 1
                num //= 10
            if digits % 2 == 0:
                count += 1
        return count
        