import importlib.util
import uuid


def generate_module(filepath: str):
    module_name = f'graybox.solution.item_{uuid.uuid4()}'

    spec = importlib.util.spec_from_file_location(module_name, filepath)

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module
