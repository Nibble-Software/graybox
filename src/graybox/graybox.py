import importlib.util
import os
import sys
import uuid

from graybox.exceptions.not_a_function_error import NotAFunctionError
from graybox.tools.generate_solution_file import generate_solution_file

status = ['PASSED', 'FAILED', 'EXECUTION_ERROR', 'FUNCTION_NOT_FOUND', 'NOT_A_FUNCTION']


def evaluate_gray_box(solution, function_name, args, expected):
    result = ''

    name = generate_solution_file(solution)

    module_name = f'graybox.solution.item_{uuid.uuid4()}'

    try:
        spec = importlib.util.spec_from_file_location(module_name, name)

        module = importlib.util.module_from_spec(spec)

        sys.modules[module_name] = module

        spec.loader.exec_module(module)

        function = getattr(module, function_name)

        if not callable(function):
            raise NotAFunctionError(function_name)

        actual = function(*args)

        result = status[0] if expected == actual else status[1]

        return {
            'status': result,
            'expected': expected,
            'got': actual
        }

    except AttributeError as error2:
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

    finally:
        os.remove(name)
