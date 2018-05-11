# -*- coding: utf-8 -*-
"""
Created on Sat May  5 03:54:59 2018

@author: thurston
"""

'''
Implement 3 different sorting algorithms (all in place):
merge sort  
quick sort: two variations, one where the pivot is the first element,
            another where the pivot is the last element
heap sort            

'''
import unittest

def mergeSort(_input):
    '''
    @_input:  a sequence of naturally comparable elements. e.g. str, int
    @return:  _input in ascending order
    '''
    length_arr = len(_input)
    
    if length_arr < 2:
        return _input
    
    left = _input[:length_arr//2]
    right = _input[length_arr//2:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge_array(left,right)

    
def merge_array(arr1, arr2):
    merged_arr = []
    left_ptr = 0
    right_ptr = 0
    while left_ptr < len(arr1) or right_ptr < len(arr2):
        if left_ptr == len(arr1):
            merged_arr.append(arr2[right_ptr])
            right_ptr += 1
        elif right_ptr == len(arr2):
            merged_arr.append(arr1[left_ptr])
            left_ptr += 1
        else:
            if arr1[left_ptr] > arr2[right_ptr]:
                merged_arr.append(arr2[right_ptr])
                right_ptr += 1
            else:
                merged_arr.append(arr1[left_ptr])
                left_ptr += 1
                
    return merged_arr
    
def inplace_mergesort(arr, head, tail):
    '''
    @arr: array
    @head: pointer
    @tail: pointer
    '''
    if tail - head <= 0:
        return
    elif tail - head == 1:
        if arr[head] > arr[tail]:
            temp = arr[head]
            arr[head] = arr[tail]
            arr[tail] = temp
    else: 
        midpoint = (head+tail)//2
        inplace_mergesort(arr, head, midpoint -1)
        inplace_mergesort(arr, midpoint, tail)
        inplace_merge(arr, head,midpoint-1,midpoint,tail)
        return

def inplace_merge(arr, head1, tail1, head2, tail2): #in place merge with arr => Worst Case O(n^2) time, O(1) auxilary space
    current = head1
    left_ptr = head1
    right_ptr = head2
    temp = None
    while current < tail2 and right_ptr<=tail2 and left_ptr <= tail2:
        if arr[left_ptr] < arr[right_ptr]: #keep everything same
            left_ptr += 1
        else: #shift insertion
            temp = arr[right_ptr]
            idx = right_ptr
            while idx > current:
                arr[idx] = arr[idx-1]
                idx -= 1
            arr[current] = temp
            right_ptr += 1
            left_ptr += 1
        current += 1
    return

def heapSort(_input):
    '''
    @_input:  a sequence of naturally comparable elements. e.g. str, int
    @return:  _input in ascending order
    '''
    max_heapify(_input)
    
    for idx2 in range(len(_input)-1,0, -1): #starting from back to front, pop off root and percolate
        temp = _input[idx2]
        _input[idx2] = _input[0]
        _input[0] = temp
        percolateDownwards(_input,0, idx2-1)
    
    
    return

def max_heapify(arr): #create heap from unsorted array
    
    #add elements left to right one by one as new leaves
    #if added element is smaller than parent, push up
    for idx in range(len(arr)):
        percolateUpwards(arr,idx)
    
    return
        

def get_heapParent(idx):
    return idx//2

def percolateDownwards(arr,current, maxPoint): #cannot percolate down arr past maxpoint
    if maxPoint < 0:
        return
    if current == maxPoint:
        return #reached endpoint
    
    leftIdx = getLeftChildIdx(current)
    leftValue = None
    rightIdx = getRightChildIdx(current)
    rightValue = None
    
    if leftIdx > maxPoint:
        leftValue = arr[current]
    else:
        leftValue = arr[leftIdx]
    if rightIdx > maxPoint:
        rightValue = arr[current]
    else: 
        rightValue = arr[rightIdx]
    if arr[current] < leftValue and leftValue > rightValue and leftIdx <= maxPoint:
        temp = arr[current]
        arr[current] = arr[leftIdx]
        arr[leftIdx] = temp
        percolateDownwards(arr, leftIdx, maxPoint)
    elif arr[current] < rightValue and rightValue > leftValue and rightIdx <= maxPoint:
        temp = arr[current]
        arr[current] = arr[rightIdx]
        arr[rightIdx] = temp
        percolateDownwards(arr, rightIdx, maxPoint)
    
    return
    
    
        

def getLeftChildIdx(idx):
    return 2*idx + 1

def getRightChildIdx(idx):
    return 2*idx + 2

def percolateUpwards(arr,idx): #moves this leaf up the tree as necessary
    if idx == 0:
        return
    
    parent_index = get_heapParent(idx)
    if arr[parent_index] < arr[idx]:
        temp = arr[idx]
        arr[idx] = arr[parent_index]
        arr[parent_index] = temp
        percolateUpwards(arr,parent_index)
    
    return
    
def quickSortFirst(_input): #inplace, no auxilary memory, 
    '''
    @_input:  a sequence of naturally comparable elements. e.g. str, int
    @return:  _input in ascending order
    '''
    inplace_quicksortfirst(_input, 0, len(_input)-1)
    return

def inplace_quicksortfirst(arr, head, tail):
    
    if tail - head < 1: 
        return
    
    elif tail - head == 1:
        if arr[head] > arr[tail]:
            temp = arr[head]
            arr[head] = arr[tail]
            arr[tail] = temp
        return
    
    pivot = arr[head] #insert later
    lower = 0
    for element in arr:
        if element < pivot:
            lower += 1
            
    #put pivot in place
    temp = arr[lower]
    arr[lower] = pivot
    arr[head]= temp

    first = head
    last = tail
    
    while first != lower and last != lower:
        if arr[first] >= pivot and arr[last] < pivot:
            temp = arr[last]
            arr[last] = arr[first]
            arr[first] = temp
            first += 1
            last -= 1
        elif arr[last] >= pivot:
            last -=1 
        elif arr[first] < pivot:
            first += 1
    inplace_quicksortfirst(arr,head, lower -1)
    inplace_quicksortfirst(arr, lower + 1, tail)
    return
        
        
def quickSortLast(_input):
    '''
    @_input:  a sequence of naturally comparable elements. e.g. str, int
    @return:  _input in ascending order
    '''
    inplace_quicksortlast(_input, 0, len(_input))
    return

def inplace_quicksortlast(arr, head, tail):
    if tail - head < 1: 
        return
    
    elif tail - head == 1:
        if arr[head] > arr[tail]:
            temp = arr[head]
            arr[head] = arr[tail]
            arr[tail] = temp
        return
    
    pivot = arr[tail] #insert later
    lower = 0
    for element in arr:
        if element < pivot:
            lower += 1
            
    #put pivot in place
    temp = arr[lower]
    arr[lower] = pivot
    arr[tail]= temp

    first = head
    last = tail
    
    while first != lower and last != lower:
        if arr[first] >= pivot and arr[last] < pivot:
            temp = arr[last]
            arr[last] = arr[first]
            arr[first] = temp
            first += 1
            last -= 1
        elif arr[last] >= pivot:
            last -=1 
        elif arr[first] < pivot:
            first += 1
    inplace_quicksortfirst(arr,head, lower -1)
    inplace_quicksortfirst(arr, lower + 1, tail)
    return

class Tester(unittest.TestCase):
    def test_mergeArray(self):
        arr1 = [1,3,5,7]
        arr2 = [2,4,6,8]
        self.assertEqual(merge_array(arr1,arr2), [1,2,3,4,5,6,7,8])
        
    def test_mergeSort(self):
        arr = [8,7,6,5,4,3,2,1]
        self.assertEqual(mergeSort(arr), [1,2,3,4,5,6,7,8])
    
    def test_inplacemerge(self):
        arr = [1,3,5,7,2,4,6,8]
        inplace_merge(arr,0,3,4,7)
        self.assertEqual(arr, [1,2,3,4,5,6,7,8])
        
    def test_inplacemerge2(self):
        arr = [6, 7, 8, 4, 5, 1, 2, 3] #[DOO]
        inplace_merge(arr,3,4,5,7)
        self.assertEqual(arr, [6,7,8,1,2,3,4,5])
        
    def test_inplacemergesort(self):
        arr = [8,7,6,5,4,3,2,1]
        inplace_mergesort(arr, 0 ,7)
        self.assertEqual(arr, [1,2,3,4,5,6,7,8])
    
    def test_inplacequicksortfirst(self):
        arr = [8,7,6,5,4,3,2,1]
        inplace_quicksortfirst(arr,0,7)
        self.assertEqual(arr, [1,2,3,4,5,6,7,8])
        
    def test_inplacequicksortlast(self):
        arr = [8,7,6,5,4,3,2,1]
        inplace_quicksortlast(arr, 0,7)
        self.assertEqual(arr,[1,2,3,4,5,6,7,8])
    
    def test_maxheapify(self):
        arr = [1,2,3,4,5,6,7,8]
        max_heapify(arr)
        self.assertEqual(arr, [8,7,6,5,4,3,2,1])
    
    def test_heapSort(self):
        arr = [8,7,6,5,4,3,2,1]
        heapSort(arr)
        self.assertEqual(arr, [1,2,3,4,5,6,7,8])

if __name__ == '__main__':
    unittest.main()

