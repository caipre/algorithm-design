#!/usr/bin/env python

import sys

array = []
with open('./.data', 'r') as f:
    for line in f:
        array.append(int(line))

def brute(arr):
    invs = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                invs += 1
    return invs

print brute(array)

def inversions(arr):
    pass

