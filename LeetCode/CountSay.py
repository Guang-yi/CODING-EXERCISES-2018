# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 17:16:01 2018

@author: Michael
"""
import unittest

class Solution(object):
    
    
    def countAndSay(self,n):
        
        """
        :type n: int
        :rtype str
        iterate starting with 1
        count each, if it changes, you count number of numbers, then encode the number that you counted, do that until you get to the nth loop
        """
 
        last = '1'
        for i in range(n-1):   
            j = 0
            currentCh = 0
            count = 1
            current = ''
            while j < len(last):
                if j+1 >= len(last) or last[currentCh]  != last[j+1]:
                    current += str(count) + last[currentCh]
                    count = 1
                    currentCh = j+1
                else:
                    count += 1
                j += 1
            last = current
        return last
                    
                    
        
        
class Tester(unittest.TestCase):
    
    def setUp(self):
        self.test = Solution()
        
    def test_null(self):
        self.assertEqual(self.test.countAndSay(1), "1")
    
    def test_leet(self):
        self.assertEqual(self.test.countAndSay(4), "1211")


if __name__ == '__main__':
    unittest.main()