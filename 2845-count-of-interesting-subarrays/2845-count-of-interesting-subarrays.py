class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n=len(nums)
        for i in range(len(nums)):
            nums[i] = 1 if nums[i] % modulo == k else 0

        prefix = 0
        frec = {0: 1}
        res = 0

        for i in range(n):
            prefix += nums[i]
            if prefix >= modulo:
                prefix -= modulo

            cur = (prefix - k + modulo) % modulo
            res += frec[cur] if cur in frec else 0
            frec[prefix] = frec.get(prefix, 0) + 1

        return res