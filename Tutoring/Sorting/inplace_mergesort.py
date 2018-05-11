# -*- coding: utf-8 -*-
"""
Created on Wed May  9 18:23:21 2018

@author: Michael
"""

def in_mergesort(l1, h, t):
    """
    Args:
        l1 LIST: Description
        h INT: Description
        t INT: Description
    
    Returns:
        LIST: Description
    """
    if t - h <= 0:
        pass
    elif t - h == 1:
        if l1[h] > l1[t]:
            swap_values(l1, h, t)
    else: 
        m = (h+t)//2
        in_mergesort(l1, h, m -1)
        in_mergesort(l1, m, t)
        in_merge(l1, h,m-1,m,t)
    return l1

def swap_values(l1, idx1, idx2):
    """
    :type l1: list
    :type idx1: integer
    :type idx2: integer
    
    Args:
        l1 LIST: Description
        idx1 INT: Description
        idx2 INT: Description
    
    Returns:
        LIST: Description
    """
    l1[idx1], l1[idx2] = l1[idx2], l1[idx1]
    return l1
    
def in_merge(l1, h1, t1, h2, t2): #in place merge with l1 => Worst Case O(n^2) time, O(1) auxilary space
    """Summary
    
    Args:
        l1 LIST: Description
        h1 INT: Description
        t1 INT: Description
        h2 INT: Description
        t2 INT: Description
    
    Returns:
        LIST: Description
    """
    curr = h1
    left = h1
    right = h2
    temp = None
    
    while curr < t2 and right<=t2 and left <= t2:
        
        if l1[left] < l1[right]:
            left += 1
        else: #shift insertion
            temp = l1[right]
            idx = right
            while idx > curr:
                l1[idx] = l1[idx-1] #shift values down
                idx -= 1
            l1[curr] = temp
            right += 1
            left += 1
        curr += 1
        
    return l1



class Tester(unittest.TestCase):

    """Summary
    """
    
    def test_inplacemerge(self):
        """Summary
        """
        l1 = [1,3,5,7,2,4,6,8]
        in_merge(l1,0,3,4,7)
        self.assertEqual(l1, [1,2,3,4,5,6,7,8])
        
    def test_inplacemerge2(self):
        """Summary
        """
        l1 = [6, 7, 8, 4, 5, 1, 2, 3] #[DOO]
        in_merge(l1,3,4,5,7)
        self.assertEqual(l1, [6,7,8,1,2,3,4,5])
        
    def test_inplacemergesort(self):
        """Summary
        """
        l1 = [8,7,6,5,4,3,2,1]
        in_mergesort(l1, 0 ,7)
        self.assertEqual(l1, [1,2,3,4,5,6,7,8])
    
if __name__ == '__main__':
    unittest.main()
