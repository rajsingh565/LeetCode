class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = math.ceil(n / 2)
        odd = n - even

        mod = ((10 ** 9) + 7)

        answer = 1
        if even:
            answer *= pow(5, even, mod)
        if odd:
            answer *= pow(4, odd, mod)
        
        return answer % mod