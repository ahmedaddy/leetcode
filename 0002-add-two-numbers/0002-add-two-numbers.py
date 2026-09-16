# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1_sum = []
        while l1.next is not None:
            l1_sum.append(l1.val)
            l1 = l1.next
        l1_sum.append(l1.val)
        l1_sum.reverse()
        l2_sum = []
        while l2.next is not None:
            l2_sum.append(l2.val)
            l2 = l2.next
        l2_sum.append(l2.val)
        l2_sum.reverse()
        l1 = "".join(str(x) for x in l1_sum)
        l2 = "".join(str(x) for x in l2_sum)
        res = [int(x) for x in list("".join(str(int(l1) + int(l2))))]
        res.reverse()
        node = ListNode(0)
        current = node
        for i, r in enumerate(res):
            current.val = r
            if (i < len(res) - 1):
                current.next = ListNode(0)
                current = current.next
        return node
