# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:23:42 2018

@author: thurston
"""

def quicksort(inp, low=0, high=-1):
    '''
    @inp:  sequence[some type that implements ]
    @low: int
    @return: 
    '''
    high = high if high != -1 else len(inp) - 1
    if (low < high):
        part = partition(inp, low, high)
        quicksort(inp, low, part)
        quicksort(inp, part + 1, high)
        
def partition(inp, low, high):
    pivot = inp[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        j -= 1
        while inp[i] < pivot:
            i += 1
        
        while inp[j] > pivot:
            j -= 1
        if i >= j:
            return j
        swap(inp, i, j)
        

def insertionSort(inp):
    i = 1
    while i < len(inp):
        j = i
        while j > 0 and inp[j - 1] > inp[j]:
            swap(inp, j - 1, j)
            j -= 1
        i += 1
        
    
def selectionSort(inp):
    n = len(inp)
    for j in range(n - 1):
        iMin = j
        for i in range(j + 1, n):
            if inp[i] < inp[iMin]:
                iMin = i
                
        if iMin != j:
            swap(inp, iMin, j)
    
            
def swap(inp, i, j):
    temp = inp[i]
    inp[i] = inp[j]
    inp[j] = temp            
            
    
