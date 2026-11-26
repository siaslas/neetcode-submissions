class WordDictionary:

    def __init__(self):
        self.root = {} 

    def addWord(self, word: str) -> None:
        curNode = self.root
        for ch in word:
            curNode.setdefault(ch, {})
            curNode = curNode[ch]
        curNode['*'] = True

    def search(self, word: str) -> bool:
        def dfs(node: dict, i: int) -> bool:
            if i == len(word):
                return node.get('*', False)
            elif word[i] == '.':
                for child in node:
                    if child != '*':
                        if dfs(node[child], i+1):
                            return True
                return False 
            elif word[i] in node:
                return dfs(node[word[i]], i+1) 
            
            return False
        
        return dfs(self.root, 0) 
