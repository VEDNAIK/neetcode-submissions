class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = []
        adjList = { i: [] for i in range(n) }
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node):
            for i in adjList[node]:
                if i not in visited:
                    visited.append(i)
                    dfs(i)
        
        components = 0

        for j in range(n):
            if j not in visited:
                components += 1
                visited.append(j)
                dfs(j)
        return components
        