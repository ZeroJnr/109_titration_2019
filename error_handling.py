#!/usr/bin/env python3
#!-*- utf-8 -*-

import sys
import math
from load_csv import load_csv

ac = len(sys.argv)

def error_handling(data_array):

    # i = 0
    # j = 0
    # while data_array[i] != '\0':
    #    while data_array[i][j] != '\n':
    #        if data_array[i][j] < '0' or data_array[i][j] > '9' or data_array[i][j] != ' ' or data_array[i][j] != ',' or data_array[i][j] != '.':
    #            sys.exit(84)
    #        j = j + 1
    #    i = i + 1
    for i in range (len(data_array)):
        if (len(data_array[i]) != 2):
            print("invalid size of data array")
            sys.exit(84)
    if len(data_array) <= 4:
        print("Invalid data into the file")
        sys.exit(84)

