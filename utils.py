'''Custom library for specific input output
'''

import os
from textwrap import wrap


def my_input(tp:object, msg:str):
    while True:
        try:
            ret = tp(input(msg))
        except ValueError:
            print(f'Please provide {tp.__name__} type data.')
            continue
        else:
            break

    return ret


def my_output(msg:str):
    # tw = terminal width
    tw = min(os.get_terminal_size().columns, 80)
    max_len = tw-6

    msg = msg.split('\n')
    row = '+' + '-'*(tw-2) + '+'
    print(row)
    for line in msg:
        if len(line) > max_len:
            chunks = wrap(line, max_len)
            for chunk in chunks:
                print('|  {}  |'.format(chunk.ljust(max_len)))
        else:
            print('|  {}  |'.format(line.ljust(max_len)))
    print(row)
