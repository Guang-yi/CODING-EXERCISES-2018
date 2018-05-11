# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:49:34 2018

@author: Michael
"""
import unittest 

def mergeSort(_input):
    """
    Args:
        _input (LIST): Description
    
    Returns:
        LIST: Description
    """
    length_list = len(_input)
    if length_list < 2:
        return _input
    
    return merge_array(mergeSort(_input[:length_list//2]),mergeSort(_input[length_list//2:]))

    
def merge_array(l1, l2):
    """
    :type l1: list
    :type l2: list
    :rtype list
    
    Args:
        l1 (LIST): Description
        l2 (LIST): Description
    
    Returns:
        LIST: Description
    """
    res = []
    
    left = 0
    right = 0
    left_len = len(l1)
    right_len = len(l2)
    
    while left < left_len and right < right_len:
        if l1[left] > l2[right]:
            res.append(l2[right])
            right += 1
        else:
            res.append(l1[left])
            left += 1

    add_rest(res, l1, left, left_len)
    add_rest(res, l2, right, right_len)
    return res

def add_rest(result, source, start, end):
    """
    Helper  to add rest of source into result from start to end indices
    
    Args:
        result (LIST): Description
        source (LIST): Description
        start (INT): Description
        end (INT): Description
    
    Returns:
        LIST: Description
    """
    while start < end:
        result.append(source[start])
        start += 1
    return result


class Tester(unittest.TestCase):

    """Summary
    """
    
    def test_mergeArray(self):
        """Summary
        """
        arr1 = [1,3,5,7]
        arr2 = [2,4,6,8]
        self.assertEqual(merge_array(arr1,arr2), [1,2,3,4,5,6,7,8])
        
    def test_mergeSort(self):
        """Summary
        """
        arr = [8,7,6,5,4,3,2,1]
        self.assertEqual(mergeSort(arr), [1,2,3,4,5,6,7,8])
    

    
if __name__ == '__main__':
    unittest.main()
