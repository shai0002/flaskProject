from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafPath(self, root: Optional[TreeNode], path: list) -> bool:
        if not root or root.val == 0:
            return False
        path.append(root.val)

        if not root.left and not root.right:
            return True
        if self.leafPath(root.left, path):
            return True
        if self.leafPath(root.right, path):
            return True
        path.pop()
        return False

    def create_tree(self, nodes, i):
        if i < len(nodes):
            if nodes[i] is None:
                return None
            root = TreeNode(nodes[i])
            root.left = self.create_tree(nodes, 2 * i + 1)
            root.right = self.create_tree(nodes, 2 * i + 2)
            return root
        return None
root = [1,2,3,4,5]
leaf = 5
s = Solution()
root_tree = s.create_tree(root, 0)
s.leafPath(root_tree,[])