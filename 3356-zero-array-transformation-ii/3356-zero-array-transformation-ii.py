class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def valid(k: int)-> bool:

            pref = [0] * (n + 1)

            for left, rght, val in queries[:k]:
                pref[left]+= val
                if rght < n:  pref[rght + 1]-= val
            
            for i in range(n):
                if nums[i] > pref[i]: return False
                pref[i+1] += pref[i]

            return True


        n, q = len(nums), len(queries)

        idx = bisect_left(range(q + 1), True, key = valid)    

        return -1 if idx > q else idx 