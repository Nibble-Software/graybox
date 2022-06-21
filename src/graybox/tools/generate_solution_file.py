import tempfile


def generate_solution_file(solution: str) -> object:
    file = tempfile.NamedTemporaryFile(prefix='solution', suffix='.py',mode='w',delete=False)
    name = file.name
    file.write(solution)
    file.close()
    return name
