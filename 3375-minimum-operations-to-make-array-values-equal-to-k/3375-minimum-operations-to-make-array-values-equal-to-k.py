class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = set()
        for i in nums:
            if(i < k):
                return -1
            elif(i > k):
                res.add(i)
        return len(res)
        