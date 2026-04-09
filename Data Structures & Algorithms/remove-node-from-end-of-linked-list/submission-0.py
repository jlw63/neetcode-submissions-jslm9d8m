# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = head
        index = 1
        #counting length
        while curr and curr.next:
            curr = curr.next
            index += 1
        
        count = 1
        remove = index - n
        if remove == 0:
            return head.next
        while l:
            if count == remove:
                l.next = l.next.next
                break

            l = l.next

            count += 1

        return head
            


        
