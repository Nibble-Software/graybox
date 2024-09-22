class NotAFunctionError(Exception):

    def __init__(self, function_name):
        self.message = f'{function_name} is not a function'

