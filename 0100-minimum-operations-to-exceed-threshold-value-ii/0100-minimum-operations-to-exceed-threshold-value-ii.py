class Solution:
    def minOperations(self, nums, k):
        heapq.heapify(nums)
        op = 0

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, x * 2 + y)
            op += 1

        return op