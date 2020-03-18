# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = None
        node = None

        while not (l1 == None and l2 == None):
            v = None
            if l1 == None:
                v = l2.val
                l2 = l2.next
            elif l2 == None:
                v = l1.val
                l1 = l1.next
            elif l1.val <= l2.val:
                v = l1.val
                l1 = l1.next
            else:
                v = l2.val
                l2 = l2.next

            if root == None:
                root = ListNode(v)
                node = root
            else:
                node.next = ListNode(v)
                node = node.next

        return root

x = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

print(x.mergeTwoLists(l1, l2))