#!/usr/bin/env python3

"""
yaml-to-py 0.0.1

A CLI tool to convert YAML file to Python module for better load performance

More info: http://github.com/szikszail/yaml-to-py
"""

import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Convert YAML configuration file to a Python module'
        'for better performance'
    )

    parser.add_argument('-i', '--input', default='input.yml',
                        help='The input Yaml file (YML or YAML)')

    args = parser.parse_args()

    print(f'Input: {args.input}')

if __name__ == "__main__":
    main()
