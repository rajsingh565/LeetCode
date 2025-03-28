class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        l1=[]
        for i in range(len(queries)):
            l1.append([queries[i],i])
        l1.sort()
        n=len(grid)
        m=len(grid[0])
        #Using BFS In this 
        #l=deque()
        op=0
        vis=[]
        for i in range(n):
            vis.append([-1]*m)
        vis[0][0]=1 
        l=[]
        heapq.heappush(l,[grid[0][0],0,0])
        dirr=[(0,1),(0,-1),(-1,0),(1,0)]
        def trace(val,op):
            while(l):
                #print(l,val,op)
                #print(l)
                vall,a,b=heapq.heappop(l)
                if vall>=val:
                    heapq.heappush(l,[vall,a,b])
                    break
                op+=1 
                for k in dirr:
                    i=a+k[0]
                    j=b+k[1]
                    if 0<=i<n and 0<=j<m and vis[i][j]!=1:
                        vis[i][j]=1 
                        heapq.heappush(l,[grid[i][j],i,j])
            return op
        opp=[0]*(len(queries))
        for k in l1:
            op=trace(k[0],op)
            opp[k[1]]=op
        return opp


        