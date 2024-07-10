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

    return list(package_dirs)


class PackageKey:
    """Priorise base packages

    Hand coded what dependencies we have along the line
    """
    def __init__(self):
        self.counter = count()
        self.core_custom_values = dict(core=1000, custom=5000)
        self.core_values   = {'math-utils' : -900, 'device-models' : -800}
        self.custom_values = {'ophyd' : -900, 'bluesky' : -800}

    def __call__(self, package_dirs: str):
        root, *t_dirs = package_dirs.split('/')
        val = self.core_custom_values[root]
        if root == 'core':
            pkg_name, = t_dirs
            try:
                val += self.core_values[pkg_name]
            except KeyError:
                pass
        if root == 'custom':
            L = len(t_dirs)
            if L == 1:
                # packages before specific machines
                val -= 4000
            elif L == 2:
                pkg_name = t_dirs[1]
                try:
                    val += self.custom_values[pkg_name]
                except KeyError:
                    pass

        return val #+ next(self.counter)


def main():
    """Traverse directories executing install for appropriate ones"""
    package_dirs = list(find_package_dirs("core/") + find_package_dirs("custom/"))
    package_dirs.sort()
    # package_dirs.sort(key=PackageKey())

    print(" ".join([f"{t_dir}/" for t_dir in package_dirs]))


if __name__ == "__main__":
    main()
