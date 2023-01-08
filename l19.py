from typing import Optional

import test


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head and head.next is None and n:
            return None

        lasts: list[ListNode] = []

        t_head: ListNode = head
        c = 0
        while t_head:
            lasts.append(t_head)
            if len(lasts) > n + 1:
                lasts = lasts[1:]
            t_head = t_head.next
            c+=1

        if c == n:
            return head.next

        if lasts:
            match len(lasts):
                case 1: lasts[0].next = None
                case 2:
                    if c == 2:
                        if n == 1:
                            lasts[0].next = None
                            return lasts[0]
                        return lasts[1]
                    lasts[0].next = None
                case _: lasts[0].next = lasts[2]

        return head


def prepare_nodes(nums: list[int]) -> Optional[ListNode]:
    nodes = [ListNode(x) for x in nums]
    if len(nums) == 1:
        return nodes[0]

    pre = nodes and nodes[-1]

    n = None
    for n in reversed(nodes[:-1]):
        n.next = pre
        pre = n

    return n


if __name__ == '__main__':
    # node, n = prepare_nodes([1,2,3,4,5]), 2
    # node, n = prepare_nodes([1]), 1
    # node, n = prepare_nodes([1, 2]), 1
    # node, n = prepare_nodes([1, 2]), 2
    # node, n = prepare_nodes([1, 2, 3]), 3
    node, n = prepare_nodes([1, 2, 3]), 1
    r = Solution.removeNthFromEnd(None, node, n)

    while r:
        print(r, end="")
        r = r.next
    print("!")
