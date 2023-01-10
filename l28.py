from dataclasses import dataclass
from typing import Iterator

import test


@dataclass
class IndInfo:
    _letters: Iterator[str]
    _target: int
    repeated: int = 0

    def __next__(self):
        return next(self._letters)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_iterator():
            yield from needle

        let_getters: dict[int, IndInfo] = {}
        for ind, c in enumerate(haystack):
            let_getters[ind] = IndInfo(get_iterator(), len(needle))

            g_indexes_to_remove = set()
            for g_ind in let_getters:
                if g_ind in g_indexes_to_remove:
                    pass
                elif c == next(let_getters[g_ind]):
                    let_getters[g_ind].repeated += 1
                    if len(needle) == let_getters[g_ind].repeated:
                        return g_ind
                else:
                    g_indexes_to_remove.add(g_ind)
            for g_ind in g_indexes_to_remove:
                let_getters.pop(g_ind)

        return -1

    def faster_strStr(self, haystack: str, needle: str) -> int:
        def get_iterator():
            yield from needle

        let_getters: dict[int, dict] = {}
        for ind, c in enumerate(haystack):
            let_getters[ind] = {"repeated": 0, "iterator": get_iterator()}

            g_indexes_to_remove = set()
            for g_ind in let_getters:
                if g_ind in g_indexes_to_remove:
                    pass
                elif c == next(let_getters[g_ind]["iterator"]):
                    let_getters[g_ind]["repeated"] += 1
                    if len(needle) == let_getters[g_ind]["repeated"]:
                        return g_ind
                else:
                    g_indexes_to_remove.add(g_ind)
            for g_ind in g_indexes_to_remove:
                let_getters.pop(g_ind)

        return -1

    def cheet_strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


def test_data():
    yield from [
        [[Solution(), "sadbutsad", "sad"], {}, 0],
        [[Solution(), "leetcode", "leeto"], {}, -1],
        [[Solution(), "abbcde", "bb"], {}, 1],
        [[Solution(), "acdebb", "bb"], {}, 4],
        [[Solution(), "acdebb", "bbb"], {}, -1],
        [[Solution(), "mississippi", "issip"], {}, 4],
    ]


if __name__ == '__main__':
    test.test(Solution.strStr, test_data())
