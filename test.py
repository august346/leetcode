from typing import Callable, Generator, Any, Optional


def test(
        f: Callable,
        f_data: Generator[tuple[list, dict, Any], None, None],
        assert_function: Optional[Callable] = None
):
    for args, kwargs, expected in f_data:
        actual = f(*args, **kwargs)
        if assert_function:
            assert_function(args, kwargs, actual, expected)
        else:
            assert actual == expected, (args, kwargs, actual, expected)
        print(f"+ {(args, kwargs, expected)}")
