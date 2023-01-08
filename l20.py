import test


def need_close_last(char: str, last: str):
    return last + char in {"()", "{}", "[]"}


class Solution:
    def isValid(self, s: str) -> bool:
        prev = ""
        for c in s:
            if prev and need_close_last(c, prev[-1]):
                prev = prev[:-1]
            else:
                prev = prev + c

        return not prev


def test_data():
    return [
        [[Solution(), "()"], {}, True],
        [[Solution(), "()[]{}"], {}, True],
        [[Solution(), "(]"], {}, False],
    ]


if __name__ == '__main__':
    test.test(Solution.isValid, test_data())
