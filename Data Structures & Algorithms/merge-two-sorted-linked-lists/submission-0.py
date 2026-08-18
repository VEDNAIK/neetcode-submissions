# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        node = temp
        while list1 and list2:
            if list1.val < list2.val:
                node.next = ListNode()
                node.next.val = list1.val
                node.next.next = list1.next
                node = node.next
                list1 = list1.next
            else:
                node.next = ListNode()
                node.next.val = list2.val
                node.next.next = list2.next
                node = node.next
                list2 = list2.next
        while list1:
            node.next = ListNode()
            node.next.val = list1.val
            node.next.next = list1.next
            node = node.next
            list1 = list1.next
        while list2:
            node.next = ListNode()
            node.next.val = list2.val
            node.next.next = list2.next
            node = node.next
            list2 = list2.next
            
        return temp.next
        