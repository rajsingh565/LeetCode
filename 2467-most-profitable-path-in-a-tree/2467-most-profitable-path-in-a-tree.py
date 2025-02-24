class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        

        bob_path = {bob: -1}
        q = deque([bob])
        visited = set([bob])
        while q:
            node = q.popleft()
            if node == 0:
                break
            
            for child in graph[node]:
                if child not in visited:
                    bob_path[child] = node
                    visited.add(child)
                    q.append(child)
        
        real_bob_path = []
        curr = 0
        while curr != -1:
            real_bob_path.append(curr)
            curr = bob_path[curr]
        


        q = deque([[0, 0]])
        visited = set()
        yegara = set()
        mx = float('-inf')

        while q:
            m = len(q)
            comp = real_bob_path.pop() if real_bob_path else -1
            for _ in range(m):
                node, alice = q.popleft()
                visited.add(node)

                if node not in yegara:
                    if node == comp:
                        temp = amount[node]//2
                        alice += temp
                    else:
                        alice += amount[node]
                
                yegara.add(node)

                is_leaf = 1
                for child in graph[node]:
                    if child not in visited:
                        is_leaf = 0
                        q.append([child, alice])
                
                if is_leaf:
                    mx = max(mx, alice)

            if comp != -1:
                yegara.add(comp)
        
        return mx