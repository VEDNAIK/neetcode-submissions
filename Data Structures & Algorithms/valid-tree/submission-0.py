class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        
        adjList = { i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for i in adjList[node]:
                if i == prev:
                    continue
                if not dfs(i, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
        