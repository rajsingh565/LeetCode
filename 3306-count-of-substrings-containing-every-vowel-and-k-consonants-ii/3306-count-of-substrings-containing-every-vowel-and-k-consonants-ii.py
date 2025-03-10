class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def countAtleastk(k):
            hs = defaultdict(int)
            vowels = set("aeiou")
            l, non_vowel, n = 0, 0, len(word)
            res = 0
            for r in range(n):
                if word[r] in vowels:
                    hs[word[r]] += 1
                else:
                    non_vowel += 1               
                while len(hs) == 5 and non_vowel >= k:
                    res += (n - r)
                    if word[l] in vowels:
                        hs[word[l]] -= 1
                    else:
                        non_vowel -= 1
                    if hs[word[l]] == 0:
                        hs.pop(word[l])
                    l += 1
            return res       
        return countAtleastk(k) - countAtleastk(k+1)