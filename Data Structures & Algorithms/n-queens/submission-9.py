class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        visited = set()
        cols, diagLeft, diagRight = set(), set(), set()
        def placeQueens(curString, placed):
            if placed == n:
                res.append([curString[i:i + n] for i in range(0, len(curString), n)])
                return
            row = len(curString) // n 
            for i in range(n): 
                if i not in cols and row + i not in diagLeft and row - i not in diagRight:
                    newRow = "." * i + "Q" + "." * (n - i - 1)
                    cols.add(i)
                    diagLeft.add(row + i)
                    diagRight.add(row - i)
                    placeQueens(curString + newRow, placed + 1)
                    cols.remove(i) 
                    diagLeft.remove(row + i)
                    diagRight.remove(row - i)
        placeQueens("", 0)
        return res