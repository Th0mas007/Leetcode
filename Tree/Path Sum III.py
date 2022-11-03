
 # https://www.youtube.com/watch?v=Vam9gldRapY
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def pathSum_a(node,targetSum):
            if not node: return 0
            res=0
            if node.val==targetSum: res+=1
            res+=pathSum_a(node.left,targetSum-node.val)
            res+=pathSum_a(node.right,targetSum-node.val)
            return res
        if not root: return 0
        return self.pathSum(root.left,targetSum)+pathSum_a(root,targetSum)+\
               self.pathSum(root.right,targetSum)