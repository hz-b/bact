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


def build_wheel(directory, wheel_directory):
    subprocess.run(["pip3", "wheel", "-v", "-w", wheel_directory, directory], check=True)


def run_command(directory):
    "Run the installation command in the specified directory"
    requirements = os.path.join(directory, "requirements.txt")
    has_requirements = False
    try:
        os.stat(requirements)
        has_requirements = True
    except FileNotFoundError:
        pass

    if has_requirements:
        try:
            subprocess.run(["pip3", "install", "-r", requirements], check=True)

        except subprocess.CalledProcessError as e:
            print(f"Error occurred while installing package requirements {requirements}: {e}")

    try:
        subprocess.run(["pip3", "install", "-e", directory], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing package in {directory}: {e}")


class PackageKey:
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
    package_dirs.sort(key=PackageKey())

    print(package_dirs)
    # for t_dir in package_dirs:
    #    print(t_dir)
    #    build_wheel(t_dir, "wheels/")

    for t_dir in package_dirs:
        run_command(t_dir)


if __name__ == "__main__":
    main()
