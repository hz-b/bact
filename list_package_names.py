import glob
import os
import subprocess
from itertools import count
from typing import Sequence


def find_package_dirs(t_dir: str):
    """Find directories containing setup.py or pyproject.toml files"""
    pyproject_files = glob.glob(f"{t_dir}**/pyproject.toml", recursive=True)
    setup_files = glob.glob(f"{t_dir}/**/setup.py", recursive=True)
    package_dirs = set()

    for file_path in pyproject_files:
        package_dirs.add(os.path.dirname(file_path))

    for file_path in setup_files:
        package_dirs.add(os.path.dirname(file_path))

    return package_dirs


def main():
    """Traverse directories listing the suitable ones"""
    package_dirs = list(find_package_dirs("core/")) + list(find_package_dirs("custom/"))
    print("\n".join([f"{t_dir}/" for t_dir in package_dirs]))


if __name__ == "__main__":
    main()
