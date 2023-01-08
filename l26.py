from copy import copy

import test


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        c_nums = copy(nums)
        storage = set()
        c = 0
        for ind, n in enumerate(c_nums):
            if n in storage:
                nums.pop(ind - c)
                c += 1
            storage.add(n)

        return len(storage)


def test_data():
    yield from [
        [[Solution(), [1,1,2]], {}, 49],
    ]


if __name__ == '__main__':
    test.test(Solution.removeDuplicates, test_data())
