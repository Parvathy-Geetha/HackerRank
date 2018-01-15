#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:12:00 2018

@author: parvathygeetha
"""
'''
Prints an array, a after 'd' left rotations
'''


def leftRotation(a, d):
    res = []
    for i in range(d,len(a)):
        res.append(a[i])
    for i in range(d):
        res.append(a[i])
    return res

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))