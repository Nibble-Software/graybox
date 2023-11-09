from graybox.graybox import evaluate_gray_box


def test_bad_sum():
    solution = '''def sumar(a,b):
    return a*b'''

    function_name = 'sumar'

    args = [2, 3]

    outputs = 5

    expected = {
        'status': 'FAILED',
        'expected': outputs,
        'got': 6
    }

    assert evaluate_gray_box(solution, function_name, args, outputs) == expected


def test_not_a_function():
    solution = '''sumar = 5'''

    function_name = 'sumar'

    args = [2, 3]

    outputs = 5

    expected = {
        'status': 'NOT_A_FUNCTION',
        'details': 'sumar is not a function'
    }

    assert evaluate_gray_box(solution, function_name, args, outputs) == expected


def test_funtion_not_found():
    solution = '''restar = 5'''

    function_name = 'sumar'

    args = [2, 3]

    outputs = 5

    expected = {
        'status': 'FUNCTION_NOT_FOUND',
        'details': 'sumar function is not on the solution'
    }

    assert evaluate_gray_box(solution, function_name, args, outputs) == expected
