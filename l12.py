import test


class Solution:
    SYMBOLS = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

    def intToRoman(self, num: int) -> str:
        result: str = ""

        c = 1
        m = 0
        while (min_c := 10 ** (c - 1)) <= num and c < 4:
            max_c = min_c * 10
            n = (to_count % max_c if (to_count := num - m) != max_c else to_count) // min_c
            if n != 0:
                x, v, i = [v for k, v in Solution.SYMBOLS.items() if (min_c <= k <= max_c)]
                result = f"{self.ex(n, x, v, i)}{result}"
            c += 1
            m += n

        if not result.startswith("M"):
            result = "M" * int(num / 1000) + result

        return result

    @staticmethod
    def ex(number: int, x: str, v: str, i: str):
        if number > 9:
            return x * int(number / 10)

        if number == 0:
            return ""

        if number <= 3:
            return i*number

        if number == 4:
            return i + v

        if number < 9:
            return v + i*(number-5)

        if number == 9:
            return i + x

        raise NotImplemented


def test_data():
    yield from [
        *[
            [[Solution(), x], {}, y]
            for x, y in reversed(list(Solution.SYMBOLS.items()))
        ],
        [[Solution(), 58], {}, "LVIII"],
        [[Solution(), 1994], {}, "MCMXCIV"],
        [[Solution(), 10000], {}, "M"*10],
    ]


if __name__ == '__main__':
    test.test(Solution.intToRoman, test_data())
