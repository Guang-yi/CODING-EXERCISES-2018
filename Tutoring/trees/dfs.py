# -*- coding: utf-8 -*-
"""
Created on Sun May 13 09:18:00 2018

@author: Michael
"""
import unittest
import tree_node
    
def dfs(root, val):
    """
        (TreeNode) root: root of a tree
        (int) value: int to be found
        return (TreeNode) with value or None if not found
    """
    if root == None:
        return None
    elif root.val == val:
        return root
    else: 
        left = dfs(root.left, val)
        right = dfs(root.right, val)
        
        if left != None:
            return left
        elif right != None: 
            return right
        return None

class Tester(unittest.TestCase): 
    def test_node(self):
        self.assertEqual(buildTree([1,2,3,None,5,6,7]).val, 1)
    def test_dfs(self):
        root = buildTree([1,2,3,None,5,6,7])
        self.assertEqual(dfs(root, 7).val, 7)

if __name__ == "__main__":
    unittest.main()