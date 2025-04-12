class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        pow10 = [1] * n
        for i in range(1, n):
            pow10[i] = pow10[i-1] * 10 % k
        ans =set()
        def rec(i, r,s):
            if i == (n + 1) // 2:
                if r!=0:
                    return
                s += s[:n//2][::-1]
                ans.add(tuple(sorted(tuple(s))))
                return 
            for d in range(9, -1 if i>0 else 0, -1):
                coeff = sum(pow10[j] for j in {i, n-1-i})
                r2 = (r + coeff * d) % k
                rec(i + 1, r2,s+str(d))
        rec(0,0,"")
        res = 0
        for s in ans:
            cnt = Counter(s)
            cur = math.factorial(n);
            for i in range(10):
                cur //=math.factorial(cnt[str(i)])
            neg = 0
            if cnt['0']:
                neg = math.factorial(n-1)
                for i in range(10):
                    if cnt[str(i)]:
                        neg //= math.factorial(cnt[str(i)]-(i==0))
            res +=cur-neg
        return res

        