import test


class Solution:
    SYMBOLS = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    def romanToInt(self, s: str) -> int:
        result = 0

        prev_max_val = 1
        for c in reversed(s):
            c_val = self.SYMBOLS[c]

            if c_val >= prev_max_val:
                prev_max_val = c_val
                result += c_val
            else:
                result -= c_val

        return result


def test_data():
    yield from [
        *[
            [[Solution(), x], {}, y]
            for x, y in reversed(list(Solution.SYMBOLS.items()))
        ],
        [[Solution(), "III"], {}, 3],
        [[Solution(), "LVIII"], {}, 58],
        [[Solution(), "MCMXCIV"], {}, 1994],
        [[Solution(), "M"*10], {}, 10000],
    ]


if __name__ == '__main__':
    test.test(Solution.romanToInt, test_data())
