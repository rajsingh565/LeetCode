class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            xroot = find(x)
            yroot = find(y)
            if xroot == yroot:
                return False
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            else:
                parent[yroot] = xroot
                if rank[xroot] == rank[yroot]:
                    rank[xroot] += 1
            return True

        for u, v, _ in edges:
            union(u, v)
        
        component_and = {}
        for u, v, w in edges:
            root = find(u)
            if root not in component_and:
                component_and[root] = w
            else:
                component_and[root] &= w
        
        answer = []
        for s, t in query:
            if find(s) != find(t):
                answer.append(-1)
            else:
                root = find(s)
                answer.append(component_and.get(root, -1))
        return answer