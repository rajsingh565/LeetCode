class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        x=Counter(nums)
        for i in x.values():
            if i%2!=0:
                return False
        return True