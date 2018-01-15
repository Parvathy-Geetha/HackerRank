#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:12:00 2018

@author: parvathygeetha
"""
'''
Print the array in reverse order
'''

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in reversed(arr):
    sys.stdout.write(str(i) + " ")


