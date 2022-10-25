# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution by Ayushi Sharma
# https://www.youtube.com/watch?v=vqaO4oIJqnI

class Solution:
    def lengthOfLinkedList(self,head):
        length=0
        temp=head
        while temp:
            temp=temp.next
            length+=1
        return length

    def reverseKGroupH(self,head,k,length):
        if length<k:
            return head
        count,nex,prev,curr=0,None,None,head
        while count<k and curr is not None:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
            count+=1
        if nex is not None:
            head.next=self.reverseKGroupH(nex,k,length-k)
        return prev


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=self.lengthOfLinkedList(head)
        return self.reverseKGroupH(head,k,length)
