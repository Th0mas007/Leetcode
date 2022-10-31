class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    # 1. Max 2 children
    # 2. left<root
    # 3. right>=root
    def createNode(self,data):
        return Node(data)

    def insert(self,node,data):
        if node is None:
           return self.createNode(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node
    
    def inorder_traversal(self,root):
        if root != None:
            self.inorder_traversal(root.left)
            print(root.data,end=" ")
            self.inorder_traversal(root.right)

tree=Tree()
root=tree.createNode(5)
# print(root.data)
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)

print('Inorder---->')
tree.inorder_traversal(root)

