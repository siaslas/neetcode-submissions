class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n, rows, cols = len(word), len(board), len(board[0])

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1),   # right
        ]

        res = False

        def dfs(visited, idx, row, col):
            nonlocal res, n, rows, cols

            if idx == n:
                res = True
                return
            
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and board[new_row][new_col] == word[idx]:
                    visited.add((row, col))
                    dfs(visited, idx+1, new_row, new_col)
                    if res == True:
                        return
                    visited.remove((row, col))
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    dfs(set(), 1, i, j)
                    if res == True:
                        return res
        
        return res