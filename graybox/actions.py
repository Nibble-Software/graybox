from typing import Any, Optional, Callable
import ast
from .status import GrayBoxStatus

__all__ = ["perform_evaluation"]


def _search_function(tree: ast.Module, code: str) -> Optional[ast.FunctionDef]:
    any_function = filter(
        lambda node: isinstance(node, ast.FunctionDef), ast.walk(tree)
    )
    possible_function = filter(lambda node: node.name == code, any_function)

    return next(possible_function, None)


def _compile_and_get_function(
    function_node: ast.FunctionDef, function_name: str
) -> Optional[Callable[[Any], Any]]:
    local_vars = {}
    global_vars = {}

    compiled_code = compile(
        ast.Module(body=[function_node], type_ignores=[]),
        "<string>",
        "exec",
        optimize=0,
    )
    exec(compiled_code, global_vars, local_vars)

    return local_vars.get(function_name)


def perform_evaluation(
    solution: str, function_name: str, args: list[Any], expected: Any
) -> tuple[GrayBoxStatus, Optional[Any]]:
    try:
        tree_code = ast.parse(solution)

        function_node = _search_function(tree_code, function_name)

        if function_node is None:
            return GrayBoxStatus.FUNCTION_NOT_FOUND, None

        function = _compile_and_get_function(function_node, function_name)
        if function is None:
            return GrayBoxStatus.NOT_A_FUNCTION, None

        if not callable(function):
            return GrayBoxStatus.NOT_A_FUNCTION, None

        actual = function(*args)

        result = GrayBoxStatus.PASSED if expected == actual else GrayBoxStatus.FAILED

        return result, actual

    except Exception as error:
        raise error
