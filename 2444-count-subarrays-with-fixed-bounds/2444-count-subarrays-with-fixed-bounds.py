class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        if minK == maxK:
            c = 0
            for num in nums:
                if num == minK:
                    c += 1
                else:
                    res += c * (c + 1) // 2
                    c = 0
            res += c * (c + 1) // 2
            return res
        minc, maxc = 0, 0
        i, j = 0, 0
        start = 0
        n = len(nums)
        for j in range(n):
            if nums[j] < minK or nums[j] > maxK:
                minc, maxc = 0, 0
                start = j + 1
                i = j + 1
                continue
            if nums[j] == minK:
                minc += 1
            elif nums[j] == maxK:
                maxc += 1
            if minc >= 1 and maxc >= 1:
                while not (minc == 1 and nums[i] == minK) and not (maxc == 1 and nums[i] == maxK):
                    if nums[i] == minK:
                        minc -= 1
                    elif nums[i] == maxK:
                        maxc -= 1
                    i += 1
                res += i - start + 1
        return res