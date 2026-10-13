class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def isPalindrome(s):
            return s == s[::-1]
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                if isPalindrome(s[i:j+1]):
                    is_palindrome[i][j] = True
        res = []
        def dfs(start, string_list):
            nonlocal n

            if start == n:
                res.append(string_list[:])
                return
            for end in range(start+1, n + 1):
                substring = s[start:end]
                if is_palindrome[start][end-1]:
                    string_list.append(substring)
                    dfs(end, string_list)
                    string_list.pop()
        
        dfs(0, [])
        return res



        

