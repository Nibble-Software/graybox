import ast
from ast import FunctionDef

from graybox.exceptions.not_a_function_error import NotAFunctionError

status = ['PASSED', 'FAILED', 'EXECUTION_ERROR', 'FUNCTION_NOT_FOUND', 'NOT_A_FUNCTION']


def evaluate_gray_box(solution, function_name, args, expected):
    try:

        tree_code = ast.parse(solution)

        global_vars = {}
        local_vars = {}

        data = ''

        try:
            function_node = next(
                node for node in ast.walk(tree_code) if isinstance(node, ast.FunctionDef) and node.name == function_name)
        except StopIteration:
            raise AttributeError

        compiled_code = compile(ast.Module(body=[function_node], type_ignores=[]), "<string>", "exec", optimize=0)

        exec(compiled_code, global_vars, local_vars)

        function = local_vars.get(function_name)

        if function is None:
            raise AttributeError(f'{function_name} not found')

        if not callable(function):
            raise NotAFunctionError(function_name)

        actual = function(*args)

        result = status[0] if expected == actual else status[1]

        return {
            'status': result,
            'expected': expected,
            'got': actual
        }

    except AttributeError:
        return {
            'status': status[3],
            'details': f'{function_name} function is not on the solution'
        }

    except NotAFunctionError as error1:
        return {
            'status': status[4],
            'details': error1.message
        }

    except Exception as error:
        raise error
