class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        def traverse(dominoes: str, target: str = 'L', stopper: str = 'R') :  
            arr, flag, counter = [], False, 0
            for i in range(len(dominoes)) : 
                if flag : 
                    if dominoes[i] == target : counter = 1 
                    elif dominoes[i] == stopper :
                        counter = 0 
                        flag = False 
                    else : counter += 1 
                if not flag :
                    if dominoes[i] == target : 
                        flag = True 
                        counter = 1
                arr.append(counter)
            return arr

        left_right = traverse(dominoes, target = 'R', stopper = 'L')
        right_left = traverse(dominoes[::-1], target = 'L', stopper = 'R')[::-1]
    
        output = ""
        for x, y in zip(left_right, right_left) : 
            if x == y : output += "."
            elif x == 0 or y == 0 : 
                if x > y : output += 'R'
                else : output += 'L'
            elif x != 0 and y != 0 : 
                if x > y : output += 'L'
                else : output += 'R'

        return output