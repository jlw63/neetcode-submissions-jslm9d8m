# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lista = head
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        listb = slow.next
        slow.next = None
        prev = None
        while listb:
            nxt = listb.next
            listb.next = prev
            prev = listb
            listb = nxt
        while prev:
            tempa = lista.next
            tempb = prev.next
            lista.next = prev
            prev.next = tempa
            lista = tempa
            prev = tempb
            



        