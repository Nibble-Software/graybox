from typing import Any, TypedDict, Optional

from .actions import perform_evaluation


class GrayBoxResult(TypedDict):
    status: str
    expected: Any
    got: Optional[Any]


def graybox(
    solution: str, function_name: str, args: list[Any], expected: Any
) -> GrayBoxResult:
    status, got = perform_evaluation(solution, function_name, args, expected)

    return GrayBoxResult(status=status.name, expected=expected, got=got)
