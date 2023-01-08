import test


BUTTONS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str, pre: str = "") -> list[str]:
        if len(digits) == 1:
            return [f"{pre}{c}" for c in BUTTONS[digits]]

        results = []
        for d in digits:
            for c in BUTTONS[d]:
                results.extend(self.letterCombinations(digits[1:], f"{pre}{c}"))
            return results

        return results


def test_data():
    yield from [
        [[Solution(), "23"], {}, ["ad","ae","af","bd","be","bf","cd","ce","cf"]],
        [[Solution(), ""], {}, []],
        [[Solution(), "2"], {}, ["a","b","c"]],
    ]


if __name__ == '__main__':
    test.test(Solution.letterCombinations, test_data())
