import sys
from types import FrameType
from typing import Any, Tuple, Optional, Callable

coverage = Tuple[str, int]

def test(num: int):
    if num > 0 and num <=30:
        num = num + 1
    elif num > 30 and num <= 60:
        num = num + 2
    else:
        num = num - 1
    return num


def traceit(frame: FrameType, event: str, arg: Any) -> Optional[Callable]:
    if event == 'line':
        global coverage
        function_name = frame.f_code.co_name
        lineno = frame.f_lineno
        coverage.append([function_name, lineno])
    return traceit

def test_traced(num: int) -> None:
    global coverage
    coverage = []
    sys.settrace(traceit)
    test(num)
    sys.settrace(None)

if __name__ == "__main__":
    test_traced(24)
    print(coverage)