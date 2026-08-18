class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = {}
        for i in range(n):
            adjlist[i] = []
        for a, b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)
        
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return
            visit.add(node)
            for i in adjlist[node]:
                if i == parent:
                    continue
                dfs(i, node)
        
        comp = 0
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                comp += 1
        return comp

# alternate methods
        # Also look at the below commented code which expalins the find by union rank method
        
        # visited = []
        # adjList = { i: [] for i in range(n) }
        # for u, v in edges:
        #     adjList[u].append(v)
        #     adjList[v].append(u)
        
        # def dfs(node):
        #     for i in adjList[node]:
        #         if i not in visited:
        #             visited.append(i)
        #             dfs(i)
        
        # components = 0

        # for j in range(n):
        #     if j not in visited:
        #         components += 1
        #         visited.append(j)
        #         dfs(j)
        # return components

        # par = [i for i in range(n)] # parent
        # rank = [1] * n

        # def find(n1):
        #     res = n1
            
        #     while res != par[res]:
        #         par[res] = par[par[res]] # path compression optional but it optimizes code also more optimal path compression in next question through recursion
        #         res = par[res]
        #     return res
        
        # def union(n1, n2):
        #     p1, p2 = find(n1), find(n2)
            
        #     if p1 == p2:
        #         return 0
            
        #     if rank[p1] > rank[p2]:
        #         par[p2] = p1
        #         rank[p1] += rank[p2]
        #     else:
        #         par[p1] = p2
        #         rank[p2] += rank[p1]
        #     return 1
        
        # res = n
        # for n1, n2 in edges:
        #     res -= union(n1, n2)
        # return res
        