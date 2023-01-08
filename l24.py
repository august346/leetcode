from typing import Optional

import test


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        r = ""
        t = self
        while t.next:
            r += f"{t.val},"
            t = t.next
        r += str(t.val)
        return r


class Solution:
    def swapPairs(
            self,
            head: Optional[ListNode],
            main: Optional[ListNode] = None,
            prev: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        if not head:
            return main or head

        if not head.next:
            return main or head

        new_fst, new_snd, trd = head.next, head, head.next.next
        new_fst.next, new_snd.next = new_snd, trd
        if prev:
            prev.next = new_fst

        return self.swapPairs(trd, main or new_fst, new_snd)


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
        [[Solution(), None], {}, None],
        [[Solution(), prepare_nodes([1])], {}, prepare_nodes([1])],
        [
            [Solution(), prepare_nodes([1,2,3,4])],
            {},
            prepare_nodes([2,1,4,3])
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
    test.test(Solution.swapPairs, test_data(), assert_f)
