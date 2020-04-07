#!/usr/bin/env python3
#!-*- utf-8 -*-

import sys
import math

def funct_derivative(data_array):
    i = 0
    deriv = []
    print("Derivative:")
    for i in range(len(data_array)):
        calc = float(data_array[i + 1][1]) - float(data_array[i - 1][1])
        calc /= (float(data_array[i + 1][0]) - float(data_array[i - 1][0]))
        deriv.append(calc)
        print("volume: %g ml -> %.2f" %(float(data_array[i][0]), deriv[i]))

