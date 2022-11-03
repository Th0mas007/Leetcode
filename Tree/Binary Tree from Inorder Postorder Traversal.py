# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(i1,i2,p1,p2):
            if i1>=i2 or p1>=p2: return None
            root=TreeNode(postorder[p2-1])
            mid=inorder.index(postorder[p2-1])
            diff=mid-i1
            root.left=helper(i1,i1+diff,p1,p1+diff)
            root.right=helper(i1+diff+1,i2,p1+diff,p2-1)
            return root
        n=len(inorder)
        return helper(0,n,0,n)
