#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:12:00 2018

@author: parvathygeetha
"""
'''
Reads n strings and stores it in an array S.

Reads q queries and prints the number of occurences of each string in S
'''
n = int(input().strip())
S = []
for i in range(n):
    S.append(input().strip())
q = int(input().strip())
for i in range(q):
    count = 0
    string = input().strip()
    for k in S:
        if(string == k):
            count = count + 1
    print(count)