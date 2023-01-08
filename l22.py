import test


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return list(self.gen("", n, 0, n))

    def gen(self, history: str, need_create: int, need_close: int, n):
        if len(history) == n*2:
            yield history

        if need_create:
            yield from self.gen(history + "(", need_create-1, need_close+1, n)

        if need_close:
            yield from self.gen(history + ")", need_create, need_close - 1, n)


def test_data():
    return [
        [[Solution(), 3], {}, ["((()))","(()())","(())()","()(())","()()()"]],
        [[Solution(), 1], {}, ["()"]],
    ]


def assert_f(*args):
    assert set(args[-2]) == set(args[-1]), args


if __name__ == '__main__':
    test.test(Solution.generateParenthesis, test_data(), assert_f)
