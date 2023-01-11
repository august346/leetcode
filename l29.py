from typing import Generator

import test


class Solution:
    iterator: Generator[str, None, None]
    divisor: int
    to_divide: str
    results: list[int]

    def divide(self, dividend: int, divisor: int) -> int:
        k_dividend, k_divisor = dividend >= 0, divisor >= 0
        self.iterator = (c for c in str(k_dividend and dividend or -dividend))
        self.divisor = k_divisor and divisor or -divisor
        self.to_divide = ""
        self.results = []

        while True:
            try:
                self.go_to_next_number()
            except StopIteration:
                break

            self.inner_divide()

        if not self.results:
            return 0

        result = int("".join(map(str, self.results)))

        result = result if k_dividend is k_divisor else -result

        if result > (x := 2**31 - 1):
            result = x
        elif result < (x := -2**31):
            result = x

        return result

    def go_to_next_number(self):
        first = True
        while int(x := self.to_divide or "0") < self.divisor:
            if first:
                first = False
            else:
                self.results.append(0)

            self.to_divide += next(self.iterator)

    def inner_divide(self):
        target = int(self.to_divide)

        c = 0
        s = 0
        while (new_s := s + self.divisor) <= target:
            c += 1
            s = new_s

        self.results.append(c)
        self.to_divide = str(target - s)


def test_data():
    yield from [
        [[Solution(), -2147483648, -1], {}, 2147483647],
        [[Solution(), 2147483648, -1], {}, -2147483648],
        [[Solution(), 2147483648, 1], {}, 2147483647],
        [[Solution(), -2147483648, 1], {}, -2147483648],
        [[Solution(), 10, 3], {}, 3],
        [[Solution(), -10, -3], {}, 3],
        [[Solution(), 7, -3], {}, -2],
        [[Solution(), -7, 3], {}, -2],
        [[Solution(), 1, 1], {}, 1],
        [[Solution(), -1, -1], {}, 1],
        [[Solution(), -1, 1], {}, -1],
        [[Solution(), 1, -1], {}, -1],
        [[Solution(), 2, 1], {}, 2],
        [[Solution(), 1, 2], {}, 0],
        [[Solution(), 2147483647, 2], {}, 1073741823],
    ]


if __name__ == '__main__':
    test.test(Solution.divide, test_data())
