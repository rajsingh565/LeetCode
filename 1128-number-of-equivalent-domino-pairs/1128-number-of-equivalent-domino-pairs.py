class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # storing all the equivalent dominoes count
        store = defaultdict(int) 
        mx = 0

        for d in dominoes:
            # Whenever an equivalent domino is encountered, 
            # storing the count
            d.sort()
            k = f"{d[0]}-{d[1]}"
            store[k] += 1

        for v in store.values():
            # for all the different equivalent domino pairs
            # calculating the possible combinations
            mx += (v*(v-1))//2
        
        return mx