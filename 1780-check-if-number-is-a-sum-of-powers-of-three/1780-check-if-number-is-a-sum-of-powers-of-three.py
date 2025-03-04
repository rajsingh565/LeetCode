class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def help(power,num):
            if num==0:
                return True
            if 3**power>num:
                return False
            add=help(power+1,num-3**power)
            skip=help(power+1,num)
            return add or skip
        return help(0,n)