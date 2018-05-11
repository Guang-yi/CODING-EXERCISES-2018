# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 17:16:13 2018

@author: Michael
"""

import unittest

class Solution(object):
    def rotateArray(self, nums, k):
        """
        double rotate method
        """
        nums.reverse()
        i = 0
        j = k - 1
        
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i +=1
            j-=1
        
        x = k
        y = len(nums)-1
        while x < y:
            temp = nums[x]
            nums[x] = nums[y]
            nums[y] = temp
            x += 1
            y -= 1
        
    
class Tester(unittest.TestCase):
    def setUp(self):
        self.nums = [1,2,3,4,5,6,7]
        self.test = Solution()
    def test_test(self):
        k = 3
        self.test.rotateArray(self.nums, k)
        self.assertEqual(self.nums,[5,6,7,1,2,3,4])

if __name__ == '__main__':
    unittest.main()