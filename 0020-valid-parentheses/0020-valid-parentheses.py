class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        l=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                l.append(i)
            else:
                if l: #to check if l is not empty 
                    # if its empty means there is no open parenthesis and 
        # directly we have closed parenthesis, so then return False

                    if i=="}" and l[-1]=="{":
                        l.pop()
                    elif i==")" and l[-1]=="(":
                        l.pop()
                    elif i=="]" and l[-1]=="[":
                        l.pop()
                    else:
                        return False
                else:
                    return False
        if l==[]:
            return True
        else:
            return False