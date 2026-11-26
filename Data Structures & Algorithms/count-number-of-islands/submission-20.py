class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        r, c = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        res = 0

        def dfs(i, j):
            visited.add((i, j))
            for dy, dx in directions:
                nr, nc = i + dy, j + dx
                if not (0 <= nr < r and 0 <= nc < c):
                    continue
                if (nr, nc) not in visited and grid[nr][nc] == '1':
                    dfs(nr, nc)
        
        for i in range(r):
            for j in range(c):
                if (i, j) not in visited and grid[i][j] == '1':
                    dfs(i, j)
                    res += 1

        return res 
        


