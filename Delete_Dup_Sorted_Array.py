# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        cur=A
        while cur.next is not None:
            if cur.next.val==cur.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return A
