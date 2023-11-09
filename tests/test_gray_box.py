from graybox.graybox import evaluate_gray_box
import time


def test_sum_code():
    solution = '''def sumar(a,b):
    return a+b'''

    function_name = 'sumar'

    args = [2, 3]

    outputs = 5

    expected = {
        'status': 'PASSED',
        'expected': outputs,
        'got': outputs
    }

    assert evaluate_gray_box(solution, function_name, args, outputs) == expected


def test_diff_code():
    solution = '''def resta(a,b):
    return a-b'''

    function_name = 'resta'

    args = [2, 3]

    output = -1

    expected = {
        'status': 'PASSED',
        'expected': output,
        'got': output
    }

    assert evaluate_gray_box(solution, function_name, args, output) == expected


def test_array_generation():
    solution = '''def generate_array(start,end):
    return list(range(start,end+1))'''

    function_name = 'generate_array'

    args = [1, 5]

    output = [1, 2, 3, 4, 5]

    expected = {
        'status': 'PASSED',
        'expected': output,
        'got': output
    }

    assert evaluate_gray_box(solution, function_name, args, output) == expected


def test_max_value():
    solution = '''def get_max_value(array):
    return max(array)'''

    function_name = 'get_max_value'

    args = [[10, 20, 1, 400, 50, 80, 3]]

    output = 400

    expected = {
        'status': 'PASSED',
        'expected': output,
        'got': output
    }

    assert evaluate_gray_box(solution, function_name, args, output) == expected
