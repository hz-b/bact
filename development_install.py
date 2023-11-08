import os
import subprocess
import glob

def find_package_dirs():
    '''Find directories containing setup.py or pyproject.toml files'''
    setup_files = glob.glob("**/setup.py", recursive=True)
    pyproject_files = glob.glob("**/pyproject.toml", recursive=True)
    package_dirs = set()

    for file_path in setup_files:
        package_dirs.add(os.path.dirname(file_path))

    for file_path in pyproject_files:
        package_dirs.add(os.path.dirname(file_path))

    return list(package_dirs)

def run_command(directory):
    '''Run the install command in the specified directory'''
    try:
        subprocess.run(["pip3", "install", "-e", directory], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing package in {directory}: {e}")

def main():
    '''Traverse directories executing install for appropriate ones'''
    package_dirs = find_package_dirs()

    for t_dir in package_dirs:
        run_command(t_dir)

if __name__ == "__main__":
    main()
