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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeKLists([list1, list2])

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if lists and all(map(lambda a: not a, lists)):
            return None

        lss: dict[int, ListNode] = {ind: l for ind, l in enumerate(filter(bool, lists))}
        ind, c = min(lss.items(), key=lambda p: p[1].val)
        last = h = ListNode(val=c.val, next=None)

        if c.next:
            lss[ind] = c.next
        else:
            lss.pop(ind)
            ind = None

        while lss:
            while isinstance(ind, int) and lss[ind].val == last.val:
                last.next = last = lss[ind]
                if lss[ind].next:
                    lss[ind] = lss[ind].next
                else:
                    lss.pop(ind)
                    ind = None

            if not lss:
                return h

            ind, _ = min(lss.items(), key=lambda p: p[1].val)
            last.next = last = lss[ind]
            if lss[ind].next:
                lss[ind] = lss[ind].next
            else:
                lss.pop(ind)
                ind = None

        return h


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


def test_data():
    return [
        [[Solution(), []], {}, None],
        [[Solution(), [[]]], {}, None],
        [
            [Solution(), list(map(prepare_nodes, [[1,4,5],[1,3,4],[2,6]]))],
            {},
            prepare_nodes([1,1,2,3,4,4,5,6])
        ],
    ]


def assert_f(*args):
    assert len(args) == 4
    l0, l1 = args[-2], args[-1]
    if l0 is None and l1 is None:
        return
    while l0 and l0.next:
        assert l0.val == l1.val
        l0, l1 = l0.next, l1.next
    assert l0.val == l1.val
    assert l0.next is l1.next and l0.next is None


if __name__ == '__main__':
    test.test(Solution.mergeKLists, test_data(), assert_f)
