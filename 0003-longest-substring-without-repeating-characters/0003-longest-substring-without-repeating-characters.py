class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        result = 0
        i = 0

        for j in range(len(s)):
             while s[j] in sett:
                sett.remove(s[i])
                i += 1
                 
             sett.add(s[j])
             result = max(result, j - i + 1)
        
        return result