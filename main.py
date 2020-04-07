#!/usr/bin/env python3
#!-*- utf-8 -*-

import sys
import math
from load_csv import load_csv
from helper import helper
from error_handling import error_handling
from derivative import funct_derivative

ac = len(sys.argv)

def helper_launch():
    if ac == 2 and sys.argv[1] == "-h":
        helper()


def main_function():
    helper_launch()
    data_array = load_csv()
    error_handling(data_array)
    funct_derivative(data_array)


if __name__ == "__main__":
    main_function()