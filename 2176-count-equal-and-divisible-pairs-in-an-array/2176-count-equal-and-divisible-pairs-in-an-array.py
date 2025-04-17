class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = defaultdict(list)
        result = 0
        for i in range(len(nums)):
            for j in count[nums[i]]:
                if (i*j) % k == 0:
                    result+=1
            count[nums[i]].append(i)
        return result 