class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabs = defaultdict(int)
        ans = 0
        for a in answers:
            ans += 1
            if rabs[a] > 0:
                rabs[a] -= 1
            else:
                rabs[a] = a
        for k in rabs.keys():
            if rabs[k] > 0:
                ans += rabs[k]
        return ans