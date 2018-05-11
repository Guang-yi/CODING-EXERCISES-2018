# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:16:11 2018

@author: Michael
"""
import unittest

#use gaussian method, mathematical solution
class Solution(object):
    def missingNumber(self, arr):
        """from value, go to index, set it negative
        In next pass, you look at all indices, if it is negative, that value exists
        If the value is zero, you look at the zero boolean
        """
        arr.append(1)
        zero = False
        for i in range(len(arr)):
            if arr[abs(arr[i])] == 0:
                zero = True
            else: 
                arr[abs(arr[i])] *= -1
        print(arr)
        num = -1 
        for j in range(len(arr)+1):
            if (arr[j] == 0 and not zero) or arr[j] < 0:
                return i
        return num
        
        
    
#Test class should all start with lowercase test
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.Solution = Solution()
    def test_LeetTestOne(self):
        self.assertEqual(self.Solution.missingNumber([3,0,1]), 2)
    
    def test_LeetTestTwo(self):
        self.assertEqual(self.Solution.missingNumber([9,6,4,2,3,5,7,0,1]), 8)
        
if __name__ == '__main__':
    unittest.main()
    
        