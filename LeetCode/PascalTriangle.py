# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 02:45:20 2018

@author: Michael
"""
import unittest 

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int 
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        FirstNumRows = [[1]]
        for i in range(2, numRows+1):
            current = [1]*i
            for j in range(i):
                if j > 0 and j< i-1:
                    current[j] = FirstNumRows[i-2][j-1]+FirstNumRows[i-2][j]
            FirstNumRows.append(current)
        return FirstNumRows

class  TestSolution(unittest.TestCase):
    def setUp(self):
        self.Solution = Solution()
    def test_null(self):
        self.assertEqual(self.Solution.generate(0), [])
        
    def test_one(self):
        self.assertEqual(self.Solution.generate(1), [[1]])
    
    def test_two(self):
        self.assertEqual(self.Solution.generate(2), [[1],[1,1]])
    def test_three(self):
        self.assertEqual(self.Solution.generate(3), [[1],[1,1],[1,2,1]])
        
    def test_four(self):
        self.assertEqual(self.Solution.generate(4), [[1],[1,1],[1,2,1],[1,3,3,1]])
    def test_five(self):
        self.assertEqual(self.Solution.generate(5), [[1],[1,1],[1,2,1],[1,3,3,1], [1,4,6,4,1]])

if __name__ == "__main__":
    unittest.main()