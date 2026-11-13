# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if l1==None :
            return l2
        if l2==None :
            return l1
        if l1.val>=l2.val:
            a=l2
            l2=l2.next
        else:
            a=l1
            l1=l1.next
        c=a
        if l1==None:
                c.next=l2
                return a
        elif l2==None:
                c.next=l1
                return a

        while l1!=None and l2!=None:
            print(c.val)
            if l1.val>=l2.val:
                c.next=l2
                c=c.next
                l2=l2.next

            else:
                c.next=l1
                c=c.next
                l1=l1.next
            if l1==None:
                c.next=l2
            elif l2==None:
                c.next=l1

        return a


        
