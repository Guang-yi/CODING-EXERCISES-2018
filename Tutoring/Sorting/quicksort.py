# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:49:40 2018

@author: Michael
"""

def quickSortFirst(_input): #inplace, no auxilary memory, 
    '''
    @_input:  a sequence of naturally comparable elements. e.g. str, int
    @return:  _input in ascending order
    
    Args:
        _input (LIST): Description
    
    Returns:
        LIST: Description
    '''
    return inplace_quicksortfirst(_input, 0, len(_input)-1)
    

def inplace_quicksortfirst(l1, head, tail):
    """Summary
    
    Args:
        l1 (LIST): Description
        head (INT): Description
        tail (INT): Description
    
    Returns:
        LIST: Description
    """
    if tail - head < 1: 
        return l1
    
    elif tail - head == 1 and l1[head] > l1[tail]:
        return swap_values(l1, head, tail)

    
    pivot = l1[head] #insert later
    count = countLessThan(l1,pivot)
            
    #put pivot in place
    swap_values(l1, count, head)
    twoPointerSwap(l1, pivot, head, tail)
    
    inplace_quicksortfirst(l1,head, count -1)
    inplace_quicksortfirst(l1, count + 1, tail)
    return l1

def countLessThan(l1, pivot):
    """Summary
    
    Args:
        l1 (LIST): Description
        pivot (INT): Description
    
    Returns:
        INT: Description
    """
    return len([elem for elem in l1 if elem < pivot])
        
    
def twoPointerSwap(l1, pivot, head, tail):
    """
    swap all values less than pivot with values greater than pivot
    
    Args:
        l1 (LIST): Description
        pivot (INT): Description
        head (INT): Description
        tail (INT): Description
    
    Returns:
        LIST: Description
    """
    first = head
    last = tail
    
    while first < last:
        if l1[first] >= pivot and l1[last] < pivot:
            swap_values(l1, first, last)
            first += 1
            last -= 1
        elif l1[last] > pivot:
            last -=1 
        elif l1[first] < pivot:
            first += 1
    return l1
    

def swap_values(l1, idx1, idx2):
    """
    :type l1: list
    :type idx1: integer
    :type idx2: integer
    
    Args:
        l1 (LIST): Description
        idx1 (INT): Description
        idx2 (INT): Description
    
    Returns:
        LIST: Description
    """
    l1[idx1], l1[idx2] = l1[idx2], l1[idx1]
    return l1
        
def quickSortLast(_input):
    '''
    @_input:  a sequence of naturally comparable elements. e.g. str, int
    @return:  _input in ascending order
    
    Args:
        _input (LIST): Description
    
    Returns:
        LIST: Description
    '''
    return inplace_quicksortlast(_input, 0, len(_input))

def inplace_quicksortlast(l1, head, tail):
    """Summary
    
    Args:
        l1 (LIST): Description
        head (INT): Description
        tail (INT): Description
    
    Returns:
        LIST: Description
    """
    if tail - head < 1: 
        return l1
    
    elif tail - head == 1 and l1[head] > l1[tail]:
        return swap_values(l1, head, tail)
    
    pivot = l1[tail] #insert later
    count = countLessThan(l1,pivot)
            
    #put pivot in place
    swap_values(l1, count, tail)
    twoPointerSwap(l1, pivot, head, tail)
            
    inplace_quicksortfirst(l1,head, count -1)
    inplace_quicksortfirst(l1, count + 1, tail)
    return l1

class Tester(unittest.TestCase):

    """Summary
    """
    
    def test_inplacequicksortfirst(self):
        """Summary
        """
        l1 = [8,7,6,5,4,3,2,1]
        inplace_quicksortfirst(l1,0,7)
        self.assertEqual(l1, [1,2,3,4,5,6,7,8])
        
    def test_inplacequicksortlast(self):
        """Summary
        """
        l1 = [8,7,6,5,4,3,2,1]
        inplace_quicksortlast(l1, 0,7)
        self.assertEqual(l1,[1,2,3,4,5,6,7,8])

if __name__ == '__main__':
    unittest.main()

