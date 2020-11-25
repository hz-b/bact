import os
import sys
import subprocess

pip = 'pip3'

args_std = [
    # '/bin/echo',
    pip,
    'install',
    '-e',
]


def process_line(stream, prefix):
    line = stream.readline()
    if line in ('', b''):
        return False
    print('% 10s> %s' % (prefix, line))
    return True


def _run_command(args):
    PIPE = subprocess.PIPE
    with subprocess.Popen(args=args, stdout=PIPE, stderr=PIPE) as proc:
        do_loop = True
        while do_loop:
            flag_err = process_line(proc.stderr, 'stderr')
            flag_out = process_line(proc.stdout, 'stdout')
            if not flag_out and not flag_err:
                break


def run_command(t_dir):

    args = args_std + [t_dir]

    print('\nExecuting command {}'.format(' '.join(args)))
    try:
        _run_command(args)
    except Exception as exc:
        print('Failed with exception {}'.format(exc))
    else:
        print('Finished\n')


def main():

    package_dirs = [
        tup[0] for tup in os.walk(os.getcwd()) if "setup.py" in tup[-1]
    ]

    for t_dir in package_dirs:
        run_command(t_dir)


if __name__ == '__main__':
    main()
