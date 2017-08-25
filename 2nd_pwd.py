#!/usr/bin/env python3

import argparse
import sys


parser = argparse.ArgumentParser(description='Get the given characters '
        'automatically for the dumbest 2 factor authentication ever.')
parser.add_argument(
        '-p',
        '--passchars',
        type=str,
        help='The character set from the email. Just copy and paste in '
        'single quites as "-p \'Jelszó:  a   s   d   f   g   h   j   k   l\'"')
parser.add_argument(
        '-a',
        '--authindicies',
        type=str,
        help='The required character indicies from the website. Copy and '
        'paste or type the comma separated list from the website e.g:'
        '"-a 1,2,3,4,5"')
args = parser.parse_args()


def get_passchars(raw):
    return list(filter(lambda c: c != "Jelszó:", raw.split()))


def get_authindicies(raw):
    return list(map(int, raw.split(',')))


def get_authchars(passchars, indicies):
    return ''.join(passchars[i-1] for i in indicies)


if __name__ == "__main__":
    passchars = get_passchars(args.passchars)
    authindicies = get_authindicies(args.authindicies)

    print(get_authchars(passchars, authindicies))

