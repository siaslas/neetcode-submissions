class PrefixTree:

    def __init__(self):
        self.root = {"end": False}

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur:
                cur[word[i]] = {"end": False}
            cur = cur[word[i]]
        cur["end"] = True

    def search(self, word: str) -> bool:
        if word[0] not in self.root:
            return False
        cur = self.root[word[0]]

        for i in range(1, len(word)):
            if word[i] not in cur:
                return False
            cur = cur[word[i]]
        return cur["end"] == True

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.root:
            return False
        cur = self.root[prefix[0]]
        for i in range(1, len(prefix)):
            if prefix[i] not in cur:
                return False
            cur = cur[prefix[i]]
        return True 
        