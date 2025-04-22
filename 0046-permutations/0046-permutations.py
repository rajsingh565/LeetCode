class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(sol):
            if len(sol)==len(nums):
                res.append(sol[:])
                return 
            for num in nums :
                if num not in sol:
                    sol.append(num)
                    backtrack(sol)
                    sol.pop()
        res=[]
        backtrack([])
        return res
        