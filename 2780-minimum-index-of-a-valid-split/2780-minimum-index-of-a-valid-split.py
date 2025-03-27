class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        l, c = len(nums), 0
        for n in nums:
            if nums.count(n) > l // 2:
                dom, total = n, nums.count(n)
                break
        for i in range(l):
            if nums[i] == dom: c += 1
            if (c > (i+1) // 2) and (total - c > (l-i-1) // 2): return i
        return -1