import tempfile


def generate_solution_file(solution: str) -> str:
    file = tempfile.NamedTemporaryFile(prefix='solution', suffix='.py', mode='w', delete=False, dir='/tmp')
    name = file.name
    file.write(solution)
    file.close()
    return name
