# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:18:37 2018

@author: Michael
"""

import unittest
import tree_node
    
def bfs(root, val):
    """
        (TreeNode) root: root of a tree
        (int) value: int to be found
        return (TreeNode) with value or None if not found
    """
    queue = []
    queue.append(root)
    while len(queue) > 0: 
        current = queue.pop()
        if current == None:
            pass
        elif current.val == val:
            return current
        else:
            queue.append(current.left)
            queue.append(current.right)
    return None

class Tester(unittest.TestCase): 
    def test_node(self):
        self.assertEqual(buildTree([1,2,3,None,5,6,7]).val, 1)
    def test_bfs(self):
        root = buildTree([1,2,3,None,5,6,7])
        self.assertEqual(bfs(root, 5).val, 5)
    def test_bfs(self):
        root = buildTree([1,2,3,None,5,6,7])
        self.assertEqual(bfs(root, 8), None)

if __name__ == "__main__":
    unittest.main()