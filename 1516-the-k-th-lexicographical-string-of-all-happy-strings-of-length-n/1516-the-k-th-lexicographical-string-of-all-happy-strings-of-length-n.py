class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        current=""
        happy_strings=[]
        self.generate_string(n,current,happy_strings)
        if len(happy_strings)<k:
            return ""
        return happy_strings[k-1]


    def generate_string(self,n,current,happy_strings):
        if len(current)==n:
            happy_strings.append(current)
            return
        
        for ch in ['a','b','c']:
            if len(current)>=1 and current[-1]==ch:
                continue
            self.generate_string(n,current+ch,happy_strings)
             