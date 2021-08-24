from termcolor import colored


def print_board(values, color):
    print(f" {colored(values['a1'],color['a1'])} | {colored(values['a2'],color['a2'])} | {colored(values['a3'],color['a3'])} \n "
          "---------\n"
          f" {colored(values['b1'],color['b1'])} | {colored(values['b2'],color['b2'])} | {colored(values['b3'],color['b3'])} \n "
          "---------\n"
          f" {colored(values['c1'],color['c1'])} | {colored(values['c2'],color['c2'])} | {colored(values['c3'],color['c3'])}")
