#! /usr/bin/env python3

import time

list_1 = [3, 1, 23, 55, 12, 43]

# FIRST VERSION

def bubble_sort(list: list):
    start = time.time()
    
    for i in range(len(list)):
        for j in range(len(list) -1):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
    print(list)
    
    end = time.time()
    print("It took " + str(end-start))

bubble_sort(list_1)

# SECOND VERSION

list_2 = [3, 1, 23, 55, 12, 43]

def bubble_sort(list: list):
    start = time.time()
    swapped = True
    
    while swapped:
        swapped = False
        for j in range(len(list) -1):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
    print(list)
    
    end = time.time()
    print("It took " + str(end-start))

bubble_sort(list_2)