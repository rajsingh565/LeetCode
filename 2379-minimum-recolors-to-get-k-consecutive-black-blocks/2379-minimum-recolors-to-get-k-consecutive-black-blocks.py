class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res=float("infinity")
        for i in range(len(blocks)-k+1):
            white=blocks[i:i+k].count('W')
            res=min(res,white)
        return res