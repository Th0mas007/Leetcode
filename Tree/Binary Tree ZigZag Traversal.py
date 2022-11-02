# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        q=[root]
        res=[]
        even_level=False
        while q:
            n=len(q)
            level=[]
            for _ in range(n):
                node=q.pop(0)
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if even_level:
                res.append(level[::-1])
            else:
                res.append(level)
            even_level=not even_level
        return res