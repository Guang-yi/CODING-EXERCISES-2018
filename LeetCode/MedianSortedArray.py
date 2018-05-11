# -*- coding: utf-8 -*-
"""
Created on Fri May 11 15:34:12 2018

@author: Michael
"""

import unittest

class Solution():
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
        start at first point in your array, take that value, where does it lie in the second array
        if that second array makes it more than half the values, you need to 
        
        just calculate the left and right side numbers
        """
        
        pass
        
        #Make nums1 smaller than nums2 to avoid OOB error


    def findBalance(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        total = len1+len2 # doesn't track if it is going to be even or odd
        
        head = 0
        tail = len1-1

        x = (head+ tail)//2
        y = self.getComplement(len1,len2,x)
        left1 = nums1[x]
        left2 = nums2[y]
        right1 = nums1[x+1]
        right2 = nums2[y+1]
        
        while left1 > right2 or left2 > right1:

            if left1 > right2: #search in left
                tail = x
            elif left2 > right1:
                head = x+1
            x = (head+ tail)//2
            y = self.getComplement(len1,len2,x)
            left1 = nums1[x]
            left2 = nums2[y]
            right1 = nums1[x+1]
            right2 = nums2[y+1]
            
            
#        if i == 0: maxLeft = nums2[hy-1]
#        elif j == 0: max_of_left = A[i-1]
#        else: max_of_left = max(A[i-1], B[j-1])    
#        maxLeft = max(left1, left2)
#        minRight = min(right1,right2)
        
        
        
        if (len(nums1) + len(nums2)) % 2 == 1:
            return maxLeft
        else:
            return (maxLeft + minRight)/2
            
    def getComplement(self, len1, len2, x):
        return (len1+len2)//2 - x
        
class Tester(unittest.TestCase):
    
    def testFindMedian(self):
        pass
    
    def test_getcomplement(self):
        s = Solution()
        self.assertEqual(s.getComplement(10,8,3),6)
        
    def test_findBalance(self):
        s = Solution()
        self.assertEqual(s.findBalance([0,1,2,3,4,5,6,7], [0,1,2,3,4,5,6,7,8,9]), 5.0)
    
    def test_findBalance2(self):
        s = Solution()
        self.assertEqual(s.findBalance([0,1,2,3,4], [0,1,2,3,4]),3.0)
    
if __name__ == "__main__":
    unittest.main()
        