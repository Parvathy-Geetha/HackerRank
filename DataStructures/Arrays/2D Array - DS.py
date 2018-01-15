#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:12:00 2018

@author: parvathygeetha
"""
'''
Find the maximum of an hourglass in a 2D-array for a 6 * 6 array.

An hourglass is defined as follows

a b c
  d
e f g
'''
import sys 

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
maximum = -sys.maxsize - 1
for i in range(1,5):
    for j in range(1,5):
        sum = arr[i][j] + arr[i - 1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
        maximum = max(sum,maximum)
        
print(maximum)