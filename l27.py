from copy import copy

import test


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        c_nums = copy(nums)
        l, c = len(nums), 0
        for ind, n in enumerate(c_nums):
            if n == val:
                nums.pop(ind - c)
                c += 1

        return l - c


def test_data():
    yield from [
        [[Solution(), [3,2,2,3], 3], {}, 2],
        [[Solution(), [0,1,2,2,3,0,4,2], 2], {}, 5],
    ]


if __name__ == '__main__':
    test.test(Solution.removeElement, test_data())