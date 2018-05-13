# -*- coding: utf-8 -*-
"""
Created on Sun May 13 09:09:09 2018

@author: Michael
"""
import unittest

class TreeNode():
    
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

def buildTree(vals, i = 0):
    """
        (List) vals: inorder list of vals; could include None
        ex. vals = [1,2,3,None,5,6,7]
    """
    if i > len(vals) -1 or vals[i] == None:
        return None
    node = TreeNode(vals[i])
    node.left = buildTree(vals,2*i+1)
    node.right = buildTree(vals,2*i+2)
    return node