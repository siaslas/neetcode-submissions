class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        res = []
        n = len(digits)

        def dfs(s, idx):
            nonlocal res, n

            if idx == n:
                res.append(s)
                return
            for ch in letters[int(digits[idx])]:
                dfs(s+ch, idx+1)
        
        if not digits:
            return []
        dfs("", 0)
        return res

