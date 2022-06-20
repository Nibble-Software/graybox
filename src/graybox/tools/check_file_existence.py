import os
import time


def check_file_existence(filepath):
    while not os.path.exists(filepath):
        time.sleep(0.5)
