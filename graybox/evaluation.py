from Enum import StrEnum

__all__ = [
    'TestStatus'
]


class TestStatus(StrEnum):
    PASSED = 'PASSED'
    FAILED = 'FAILED'
    EXECUTION_ERROR = 'EXECUTION_ERROR'
    FUNCTION_NOT_FOUND = 'FUNCTION_NOT_FOUND'
    NOT_A_FUNCTION = 'NOT_A_FUNCTION'
