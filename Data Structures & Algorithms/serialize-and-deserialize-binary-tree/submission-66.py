# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        s = ""
        q = deque([root])
        nextLvl = []

        while q:
            while q:
                node = q.popleft()

                if not node:
                    s += "N,"
                    continue
                else:
                    s += str(node.val) + ","
                nextLvl.append(node.left)
                nextLvl.append(node.right)
            
            q.extend(nextLvl)
            nextLvl.clear()
        
        return s[:-1]
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        values = data.split(",")
        n = len(values)
        j = 1
        
        for i in range(n):
            if values[i] == "N":
                continue
            if type(values[i]) == str:
                values[i] = TreeNode(int(values[i]))
            if j < n and values[j] != "N":
                values[i].left = TreeNode(int(values[j]))
                values[j] = values[i].left
            if j+1 < n and values[j+1] != "N":
                values[i].right = TreeNode(int(values[j+1]))
                values[j+1] = values[i].right
            j += 2
            
        return values[0]



        
