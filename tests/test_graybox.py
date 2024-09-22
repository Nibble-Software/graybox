import os
from graybox.graybox import graybox


def _read_file_content(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def test_passed_add() -> None:
    passed_add_path = os.path.join(
        os.path.dirname(__file__), "resources", "passed_add.py"
    )

    solution = _read_file_content(passed_add_path)
    arguments = [2, 3]
    function_result = 5
    expected = {"status": "PASSED", "expected": function_result, "got": function_result}

    result = graybox(solution, "add", arguments, function_result)

    assert result == expected


def test_failed_add() -> None:
    failed_add_path = os.path.join(
        os.path.dirname(__file__), "resources", "failed_add.py"
    )

    solution = _read_file_content(failed_add_path)
    arguments = [2, 3]
    function_result = 5
    expected = {"status": "FAILED", "expected": function_result, "got": 6}

    result = graybox(solution, "add", arguments, function_result)

    assert result == expected


def test_add_not_found() -> None:
    not_a_function_path = os.path.join(
        os.path.dirname(__file__), "resources", "no_add.py"
    )

    solution = _read_file_content(not_a_function_path)
    arguments = [2, 3]
    function_result = 5
    expected = {
        "status": "FUNCTION_NOT_FOUND",
        "expected": function_result,
        "got": None,
    }

    result = graybox(solution, "add", arguments, function_result)

    assert result == expected
