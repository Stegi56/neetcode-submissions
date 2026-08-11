# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialised = ""
        def dfs(n: Optiona[TreeNode]) -> None:
            nonlocal serialised
            if n:
                serialised += str(n.val) + ","
                dfs(n.left)
                dfs(n.right)
                return
            else:
                serialised += "N,"
        dfs(root)
        return serialised

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        c = 0
        def dfs() -> Optional[TreeNode]:
            nonlocal c
            val = ""
            while c < len(data):
                char = data[c]
                c += 1
                if char == ",":
                    break
                else:
                    val += char
            
            if val == "N" or "":
                return None
            else:
                return TreeNode(int(val), dfs(), dfs())

        return dfs()
        
