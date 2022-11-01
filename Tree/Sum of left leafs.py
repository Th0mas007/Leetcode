# At any node, check if the left child is a leaf.
# if yes -> return the left leaf child's value + any left leaf children in the right sub-tree
# if no -> bummer. gotta check in the right sub-tree for any left leaf children

# Also, we cannot enter a node and then determine whether it was a left child. For this, one may want to pass a flag variable. If we want to avoid any passing of variables, we need to look down from a parent node at its children node.

# Therefore our smallest unit for consideration becomes a node and its immediate children.

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # does this node have a left child which is a leaf?
        if root.left and not root.left.left and not root.left.right:
			# gotcha
            return root.left.val + self.sumOfLeftLeaves(root.right)

        # no it does not have a left child or it's not a leaf
        else:
			# bummer
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
