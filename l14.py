import test


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""

        gen = zip(*strs)
        for x in gen:
            if len(set(x)) == 1:
                result += x[0]
            else:
                return result

        return result


def test_data():
    yield from [
        [[Solution(), ["flower","flow","flight"]], {}, "fl"],
        [[Solution(), ["dog","racecar","car"]], {}, ""],
        [[Solution(), ["a"]], {}, "a"],
    ]


if __name__ == '__main__':
    test.test(Solution.longestCommonPrefix, test_data())
