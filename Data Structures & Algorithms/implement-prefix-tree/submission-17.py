class PrefixTree:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            cur = cur.setdefault(ch, {})
        cur["#"] = True  # end-of-word marker

    def _walk(self, s: str):
        cur = self.root
        for ch in s:
            if ch not in cur:
                return None
            cur = cur[ch]
        return cur

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and "#" in node

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None 
        