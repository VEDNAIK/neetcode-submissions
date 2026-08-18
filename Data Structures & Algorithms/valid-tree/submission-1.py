class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        adjlist = {}
        for i in range(n):
            adjlist[i] = []
        
        for a, b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)
        
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)
            for i in adjlist[node]:
                if i == parent:
                    continue
                if dfs(i, node) == False:
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
