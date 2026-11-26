class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        rows, cols = len(board), len(board[0])
        self.trie = {}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        res = []

        def buildTrie(word):
            curNode = self.trie
            for ch in word:
                curNode = curNode.setdefault(ch, {})
            curNode['*'] = word
        
        def dfs(r, c, node):
            if '*' in node:
                res.append(node.pop('*')) 
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                next_ch = board[nr][nc]
                if (nr, nc) not in visited and next_ch in node:
                    dfs(nr, nc, node[next_ch])
            visited.remove((r, c))
        for word in words:
            buildTrie(word)     
 
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in self.trie:
                    dfs(i, j, self.trie[board[i][j]])
        return res

