#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:12:00 2018

@author: parvathygeetha
"""
'''
Assigns a variable lastAnswer = 0
Declare a list of 'n' empty sequences.
Performs the following operations based on the Query No.

Query: 1 x y
 1. Find the sequence number,seq = (x ^ lastAnswer) % n
 2. Append integer y to sequence, seq
Query: 2 x y
 1. Find the sequence number,seq = (x ^ lastAnswer) % n
 2. Find the value of element in y % size (where  is the size of sequence, seq) and assign it to lastAnswer
 3. Print the new value of lastAnswer on a new line
'''
lastAnswer = 0
n, q = input().strip().split(' ');
n,q = int(n), int(q)
S = [[] for i in range(n)]

for i in range(q):
    arr = []
    for i in input().strip().split(' '):
        arr.append(int(i))
    if(arr[0] == 1):
        seq = (arr[1] ^ lastAnswer) % n
        S[seq].append(arr[2])
    
    if(arr[0] == 2):
        seq = (arr[1] ^ lastAnswer) % n
        val = arr[2] % len(S[seq])
        lastAnswer = S[seq][val]
        print(lastAnswer)