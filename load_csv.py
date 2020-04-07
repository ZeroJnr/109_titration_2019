#!/usr/bin/env python3
#!-*- utf-8 -*-

import sys
import math
import csv

ac = len(sys.argv)

def check_param():
    if ac != 2:
        print("false arguments")
        sys.exit(84)


def load_csv():
    check_param()
    data_array = []
    try:
        with open(sys.argv[1], 'r') as fd:
            data = csv.reader(fd, delimiter=';')
            data_array = list(data)
    except:
        print("error when open the file")
        sys.exit(84)
    return data_array

