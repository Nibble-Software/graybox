import os
from random import randrange

from graybox.tools.get_file_separator import get_file_separator
from graybox.tools.generate_solution_file import generate_solution_file
from graybox.exceptions.not_a_function_error import NotAFunctionError
from graybox.tools.check_file_existence import check_file_existence

status = ['PASSED', 'FAILED', 'EXECUTION_ERROR', 'FUNCTION_NOT_FOUND', 'NOT_A_FUNCTION']


def evaluate_gray_box(solution, function_name, args, expected):
    result = ''

    path = os.path.dirname(os.path.abspath(__file__))

    separator = get_file_separator()

    module_name = f'white_box_solution_{randrange(10000)}'

    package_name = 'graybox'

    module_path = f'{package_name}.{module_name}'

    solution_file_path = f'{path}{separator}{module_name}'

    generate_solution_file(solution_file_path, solution)

    check_file_existence(f'{solution_file_path}.py')

    try:
        package, imported = force_import(module_path, package_name)

        while not imported:
            os.path.exists(f'{solution_file_path}.py')

            print(f'{solution_file_path}.py')

            package, imported = force_import(module_path, package_name)

        function = getattr(package, function_name)

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
        os.remove(f'{path}{separator}{module_name}.py')


def force_import(module_path, package_name):
    try:
        package = __import__(module_path, locals(), globals(), fromlist=[package_name])
        return package, True
    except ModuleNotFoundError as error:
        return None, False
