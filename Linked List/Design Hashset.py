class ListNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
class MyHashSet:

    def __init__(self):
        self.size=1000
        self.m=[False]*self.size
        

    def add(self, key: int) -> None:
        index=key%self.size
        if self.m[index] is None:
            self.m[index]=ListNode(key,True)
        else:
            currNode=self.m[index]
            self.m[index]=ListNode(key,True)
            self.m[index].next=currNode
        

    def remove(self, key: int) -> None:
        index=key%self.size
        if self.m[index] is None:
            return
        else:
            currNode=self.m[index]
            while currNode:
                if currNode.key==key:
                    currNode.val=False
                    break
                currNode=currNode.next

    def contains(self, key: int) -> bool:
        index=key%self.size
        if self.m[index] is None:
            return False
        else:
            currNode=self.m[index]
            while currNode:
                if currNode.key==key:
                    if currNode.val==True:
                        return True
                    else:
                        return False
                currNode=currNode.next
            return False
                        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
