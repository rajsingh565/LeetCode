class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        ans = [[] for i in range(n)]
        heapify(people)
        while people:
            height,pos = heappop(people)
            k = pos
            i = 0
            while k or ans[i]!=[]:
                if ans[i]==[] or ans[i][0]>=height:
                    k-=1
                i+=1
            ans[i] = [height,pos]
        return ans