class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = {node: [] for node in range(n)}
        for seq in roads:
            sr,dest,dist= seq[0], seq[1],seq[2]
            graph[sr].append((dest,dist))
            graph[dest].append((sr,dist))
        distance=[float("inf") for i in range(n)]
        ways=[0 for i in range(n)]
        q = []
        mod=int(1e9 + 7)
        heapify(q)
        distance[0]=0
        ways[0]=1
        heappush(q,(0,0))
        while q:
            item=heappop(q)
            prevdis=item[0]
            prevnode=item[1]
            for i in graph[prevnode]:
                currNode=i[0]
                currWt=i[1]
                if prevdis+currWt<distance[currNode]:
                    distance[currNode]=prevdis+currWt
                    ways[currNode]=ways[prevnode]
                    heappush(q,(prevdis+currWt,currNode))

                elif  prevdis+currWt== distance[currNode]:
                    ways[currNode]=int((ways[currNode]+ways[prevnode])%mod)

        return ways[n-1]%mod