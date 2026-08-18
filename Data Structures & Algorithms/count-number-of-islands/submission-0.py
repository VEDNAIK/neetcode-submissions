class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0
        directions = [[1, 0], [0 , 1], [-1, 0], [0, -1]]

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r >= 0 and r < ROWS
                        and c >= 0 and c < COLS
                        and (r, c) not in visited
                        and grid[r][c] == "1"):
                        visited.add((r, c))
                        q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands