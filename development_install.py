'''Simple script executing development install for packages in sub directories
'''

import os
import subprocess

#: to be on the save side ... ymmv
pip = 'pip3'

#: pip and its the development install commands
args_std = [
    # '/bin/echo',
    pip, 'install', '-e',
]


def _run_command(args):
    PIPE = subprocess.PIPE
    with subprocess.Popen(args=args, stdout=PIPE, stderr=PIPE) as proc:
        while not proc.returncode:
            output = errs = None
            try:
                output, errs = proc.communicate(timeout=1)
            except subprocess.TimeoutExpired:
                pass
            except ValueError:
                # No more reads
                return
            if errs:
                print('Got errors {}'.format(errs))
                return

            if output:
                output = output.decode()
                print(output)


def run_command(t_dir):
    args = args_std + [t_dir]

    print('\nExecuting command {}'.format(' '.join(args)))
    try:
        _run_command(args)
    except Exception as exc:
        print('Failed with exception {} type {}'.format(exc, repr(exc)))
    else:
        print('Finished\n')


def main():
    '''traverse directories executing install for appropriate ones

    for each where a setup.py is found
    '''
    package_dirs = [
        tup[0] for tup in os.walk(os.getcwd()) if "setup.py" in tup[-1]
    ]

    for t_dir in package_dirs:
        run_command(t_dir)


if __name__ == '__main__':
    main()
