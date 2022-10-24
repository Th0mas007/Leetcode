class ListNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
class MyHashMap:

    def __init__(self):
        self.size=1000
        self.m=[None]*self.size
        

    def put(self, key: int, val: int) -> None:
        index=key%self.size
        if self.m[index] is None:
            self.m[index]=ListNode(key,val)
        else:
            currNode=self.m[index]
            self.m[index]=ListNode(key,val)
            self.m[index].next=currNode
        

    def get(self, key: int) -> int:
        index=key%self.size
        if self.m[index] is None:
            return -1
        else:
            currNode=self.m[index]
            while currNode:
                if currNode.key==key:
                    if currNode.val is None:
                        return -1
                    else:
                        return currNode.val
                currNode=currNode.next
            return -1
        

    def remove(self, key: int) -> None:
        index=key%self.size
        if self.m[index] is None:
            return
        else:
            currNode=self.m[index]
            while currNode:
                if currNode.key==key:
                    currNode.val=None
                    break
                currNode=currNode.next        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
