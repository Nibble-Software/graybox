import platform


def get_file_separator():
    return '\\' if 'Windows' in platform.platform() else '/'
