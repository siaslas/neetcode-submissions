class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(leftParen, rightParen, curString):
            if rightParen == n:
                res.append(curString)
                return
            if curString[-1] == "(":
                if leftParen < n:
                    dfs(leftParen+1, rightParen, curString[:] + "(")
                dfs(leftParen, rightParen+1, curString[:] + ")")
            else:
                if leftParen < n:
                    dfs(leftParen+1, rightParen, curString[:] + "(")
                if leftParen > rightParen:
                    dfs(leftParen, rightParen+1, curString[:] + ")")

        dfs(1, 0, "(")
        return res

            
