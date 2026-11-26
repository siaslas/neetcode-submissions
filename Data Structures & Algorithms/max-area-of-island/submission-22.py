class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        r, c = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        max_area, cur_area = 0, 0

        def dfs(i, j):
            nonlocal max_area, cur_area
            visited.add((i, j))
            max_area = max(max_area, cur_area)

            for dy, dx in directions:
                nr, nc = i + dy, j + dx
                if not (0 <= nr < r and 0 <= nc < c):
                    continue
                if (nr, nc) not in visited and grid[nr][nc] == 1:
                    cur_area += 1
                    dfs(nr, nc)
        
        for i in range(r):
            for j in range(c):
                if (i, j) not in visited and grid[i][j] == 1:
                    cur_area = 1
                    dfs(i, j)

        return max_area 
 