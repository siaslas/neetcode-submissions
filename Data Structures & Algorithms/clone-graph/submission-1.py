"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        if not node.neighbors:
            return Node(node.val)

        g1, g2 = node, Node(node.val)
        mp = {g1: g2}

        def dfs(g1, g2):
            adj_list = []

            for neighbor in g1.neighbors:
                if neighbor not in mp:
                    new_node = Node(neighbor.val)
                    mp[neighbor] = new_node
                    adj_list.append(new_node)
                    dfs(neighbor, new_node)
                else:
                    adj_list.append(mp[neighbor])
            
            g2.neighbors = adj_list
                
        dfs(g1, g2)
        return mp[node]