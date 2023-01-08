import test


# TODO
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_set = set()
        s_nums = list(sorted(nums))

        li, mi, ri = 0, 1, len(s_nums) - 1
        l, m, r = [s_nums[x] for x in [li, mi, ri]]
        prev_l, prev_r = None, None

        while li < ri:
            if prev_r == r:
                ri -= 1
                prev_r = r
                r = s_nums[ri]
                continue
            if prev_l == l:
                li += 1
                prev_l = l
                l = s_nums[li]
                continue
            if -(l*2) < r:
                ri -= 1
                prev_r = r
                r = s_nums[ri]
                continue
            if r*2 < -l:
                li += 1
                prev_l = l
                l = s_nums[li]
                continue

            result_set.update(self.find_all(s_nums[li:ri+1]))

            if -l > r:
                li += 1
                prev_l = l
                l = s_nums[li]
                continue
            if -l < r:
                ri -= 1
                prev_r = r
                r = s_nums[ri]
                continue

            li, ri = li + 1, ri - 1
            prev_l, prev_r = l, r
            l, r = s_nums[li], s_nums[ri]

        return list(map(list, result_set))

    def find_all(self, nums: list[int], l):
        for ri in reversed(range(len(nums))):
            r = nums[ri]
            for mi in range(0, ri):
                m = nums[mi]
                if l + m + r == 0:
                    yield l, m, r
                    break


def test_data():
    yield from [
        # [[Solution(), [-1,0,1,2,-1,-4]], {}, [[-1,-1,2],[-1,0,1]]],
        # [[Solution(), [-2,0,1,1,2]], {}, [[-2,0,2],[-2,1,1]]],
        # [[Solution(), [1,2,-2,-1]], {}, []],
        # [[Solution(), [1,1,-2]], {}, [[-2,1,1]]],
        [[Solution(), [-1,0,1,2,-1,-4,-2,-3,3,0,4]], {}, [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]],
    ]


if __name__ == '__main__':
    test.test(Solution.threeSum, test_data())


# -2, -2, -1, -1, 0, 0, 0, 1, 1, 2, 3, 4, 5, 6
