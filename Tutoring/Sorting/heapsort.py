# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:49:49 2018

@author: Michael
"""

def heapSort(_input):
    '''
    Args:
        _input (LIST): UNSORTED ITERABLE
    
    Returns:
        LIST: SORTED ITERABLE
    '''
    max_heapify(_input)
    
    for idx in range(len(_input)-1,0, -1): #starting from back to front, pop off root and percolate
        swap_values(_input, 0, idx)
        percolateDownwards(_input,0, idx-1)

    return _input

def swap_values(l1, idx1, idx2):
    """
    Args:
        l1 (LIST): COMPARABLE
        idx1 (INT): index
        idx2 (INT): swap index
    
    Returns:
        LIST: original list
    """
    l1[idx1], l1[idx2] = l1[idx2], l1[idx1]
    return l1

def max_heapify(l1): #create heap from unsorted array
    """Summary
    
    Args:
        l1 (List): unheaped list
    
    Returns:
        List: heap list
    """
    #add elements left to right one by one as new leaves
    #if added element is smaller than parent, push up
    for idx in range(len(l1)):
        percolateUpwards(l1,idx)
    return l1
        

def get_heapParent(idx):
    """
    Args:
        idx (INT): parent index of idx in an array backed heap
    
    Returns:
        INT: parent index
    """
    return idx//2

def percolateDownwards(l1,current, maxIndex): #cannot percolate down l1 past maxIndex
    """Summary
    
    Args:
        l1 (LIST): Description
        current (INT): Description
        maxIndex (INT): Description
    
    Returns:
        LIST: Description
    """
    if maxIndex < 0 or current == maxIndex:
        return l1
    
    #Determine what is larger, root, left child, or right child
    nextChild = nextIndexDown(l1,current, maxIndex)
    if nextChild != -1:
        swap_values(l1,current, nextChild)
        percolateDownwards(l1, nextChild, maxIndex)
    
    return l1

def nextIndexDown(l1, current, maxIndex): #returns next index to percolate down to, return -1 if nothing
    """Summary
    
    Args:
        l1 (LIST): Description
        current (INT): Description
        maxIndex (INT): Description
    
    Returns:
        INT: Description
    """
    left = getLeft(current)
    leftValue = l1[current] if left > maxIndex else l1[left]
    
    right = getRight(current)
    rightValue = l1[current] if right > maxIndex else l1[right]
    
    if l1[current] < leftValue and leftValue > rightValue and left <= maxIndex:
        return left
    elif l1[current] < rightValue and rightValue > leftValue and right <= maxIndex:
        return right
    
    return -1

def getLeft(idx):
    """Summary
    
    Args:
        idx (INT): Description
    
    Returns:
        INT: Description
    """
    return 2*idx + 1

def getRight(idx):
    """Summary
    
    Args:
        idx (INT): Description
    
    Returns:
        INT: Description
    """
    return 2*idx + 2

def percolateUpwards(l1,idx): #moves this leaf up the tree as necessary
    """Summary
    
    Args:
        l1 (LIST): Description
        idx (INT): Description
    
    Returns:
        list: Description
    """
    if idx == 0:
        return L1
    
    parent_index = get_heapParent(idx)
    if l1[parent_index] < l1[idx]:
        swap_values(l1, idx, parent_idx)
        percolateUpwards(l1,parent_index)
    return l1

class Tester(unittest.TestCase):

    """Summary
    """
    
    def test_heapSort(self):
        """Summary
        """
        l1 = [8,7,6,5,4,3,2,1]
        heapSort(l1)
        self.assertEqual(l1, [1,2,3,4,5,6,7,8])

if __name__ == '__main__':
    unittest.main()

