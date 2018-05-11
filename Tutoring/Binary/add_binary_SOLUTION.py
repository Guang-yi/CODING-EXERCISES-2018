# -*- coding: utf-8 -*-
"""
Created on Tue May  1 17:27:18 2018

@author: Michael
"""

import unittest 


class Solution(object):
    
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if(len(a) < len(b)):
            addBinary(b, a)
        
        a = a[::-1]
        b = b[::-1]
        
        aPtr = 0
        bPtr = 0
        
        total = ""
        carry = 0
        while aPtr < len(a):
            aVal = a[aPtr]
            if aPtr > len(b)-1:
                bVal = 0
            sumBit =  aVal + bVal + carry
            carry = sumBit /2
            total += str(sumBit % 2)
            a += 1
        return total
        
        