class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        def recursive(path, choose):
            ans.add(path)
            if not choose: return
            for i in range(len(choose)):
                recursive(path + choose[i], choose[:i] + choose[i+1:])
        recursive("", tiles)
        return len(ans) - 1