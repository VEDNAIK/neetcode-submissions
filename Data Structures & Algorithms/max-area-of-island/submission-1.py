class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        maxarea = 0

        def bfs(r, c, area):
            q = collections.deque()
            visited.add((r, c))
            q.append((r,c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (0 <= row < ROWS
                        and 0 <= col < COLS and
                        (row, col) not in visited and
                        grid[row][col] == 1):
                        q.append((row, col))
                        visited.add((row, col))
                        area += 1
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c, 1)
                    maxarea = max(maxarea, area)
        return maxarea
        

        