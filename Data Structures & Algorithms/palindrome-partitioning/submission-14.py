class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]
        
        res = []
        
        def dfs(start, string_list):
            if start == len(s):
                res.append(string_list[:])
                return
            for end in range(start+1, len(s) + 1):
                substring = s[start:end]
                if isPalindrome(substring):
                    string_list.append(substring)
                    dfs(end, string_list)
                    string_list.pop()
        
        dfs(0, [])
        return res



        

