class Solution:
    def countAndSay(self, n: int) -> str:
        
        def solve(x):
            if x == 1:
                return '1'
            
            new = ''
            old = solve(x-1)

            prev = old[0]
            count = 0 

            for i in range(len(old)):
                if prev == old[i]:
                    count += 1 
                else:
                    new += (str(count))
                    new += (prev)
                    prev = old[i]
                    count = 1 
                
            new += (str(count))
            new += (prev)
            
            return new

        return solve(n)