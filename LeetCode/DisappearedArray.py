# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 16:49:39 2018

@author: Michael
"""

import unittest

class Solution:
    
    def disappearNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res

class Tester(unittest.TestCase):
    def setUp(self):
        self.test = Solution()
    
    def test_null(self):
        self.assertEqual(self.test.disappearNumber([]),[])
    
    def test_one(self):
        self.assertEqual(self.test.disappearNumber([4,3,2,7,8,2,3,1]),[5,6])

if __name__ == "__main__":
    unittest.main()