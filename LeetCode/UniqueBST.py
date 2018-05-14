# -*- coding: utf-8 -*-
"""
Created on Sun May 13 19:56:23 2018

@author: Michael
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [None] * (n + 1)
        table[0] = 1
        table[1] = 1
        
        for i in range(2,n+1):
            sum = 0
            for j in range(0, i):
                sum += table[j] * table[i-j-1]
            table[i] = sum
        return table[n]
            