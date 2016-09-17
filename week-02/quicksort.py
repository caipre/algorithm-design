#!/usr/bin/env python

from random import randint

def quicksort(a):
    if len(a) < 2:
        return a
    elif len(a) == 2:
        if a[1] < a[0]:
            a[0], a[1] = a[1], a[0]
        return a

    pivot = randint(0, len(a) - 1)
    if pivot != 0:
        a[0], a[pivot] = a[pivot], a[0]
        pivot = 0

    i = 1
    for j in range(1, len(a)):
        if a[j] < a[pivot]:
            a[j], a[i] = a[i], a[j]
            i += 1

    a[i-1], a[pivot] = a[pivot], a[i-1]

    a[:i] = quicksort(a[:i])
    a[i+1:] = quicksort(a[i+1:])
    return a

print quicksort(array)
