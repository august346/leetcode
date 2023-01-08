import test


class Solution:
    def maxArea(self, height: list[int]) -> int:
        s_height = {
            ind: h for ind, h
            in sorted(enumerate(height), key=lambda pp: pp[1], reverse=True)
        }

        c = 2
        tmp = []
        for k in s_height:
            if not c:
                break
            tmp.append(k)
            c -= 1

        li, ri = min(tmp), max(tmp)
        l, r = s_height[li], s_height[ri]
        s = min(l, r) * (ri - li)

        c = 0
        for ind, target_h in s_height.items():
            if c < 2:
                c += 1
                continue

            li, ri = min(ind, li), max(ind, ri)

            s = max(s, target_h * (ri - li))

        return s


def test_data():
    yield from [
        [[Solution(), [1,8,6,2,5,4,8,3,7]], {}, 49],
        [[Solution(), [1,1]], {}, 1],
        [[Solution(), [8,10,14,0,13,10,9,9,11,11]], {}, 80],    # 53
        [[Solution(), [1,2,4,3]], {}, 4],     # 52
        [[
            Solution(),
            [76, 155, 15, 188, 180, 154, 84, 34, 187, 142, 22, 5, 27, 183, 111, 128, 50, 58, 2, 112, 179, 2, 100, 111,
             115, 76, 134, 120, 118, 103, 31, 146, 58, 198, 134, 38, 104, 170, 25, 92, 112, 199, 49, 140, 135, 160, 20,
             185, 171, 23, 98, 150, 177, 198, 61, 92, 26, 147, 164, 144, 51, 196, 42, 109, 194, 177, 100, 99, 99, 125,
             143, 12, 76, 192, 152, 11, 152, 124, 197, 123, 147, 95, 73, 124, 45, 86, 168, 24, 34, 133, 120, 85, 81,
             163, 146, 75, 92, 198, 126, 191]
        ], {}, 18048],     # 57
    ]


if __name__ == '__main__':
    test.test(Solution.maxArea, test_data())
