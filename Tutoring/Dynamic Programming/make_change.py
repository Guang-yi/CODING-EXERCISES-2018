# -*- coding: utf-8 -*-
"""
Created on Thu May 10 07:07:37 2018

@author: Michael Lee
"""
import unittest

IMPOSSIBLE_AMOUNT = (-1,-1)
BASE = (0,0)
UNTOUCHED = None
NO_COIN = -1

def minCoin(coinList, amount):
    table = _initializeTable(amount)
    return _getMinCoin(coinList, amount, table)[0]

def getChange(coinList, amount):
    table = _initializeTable(amount)
     #populate table
    _getMinCoin(coinList, amount, table)

    #table traceback, accumulate coins
    current = table[amount]
    coins = []
    #BASE represents end of traceback
    while (current > BASE):
        coin = current[1]
        coins.append(coin) #accumulate coins
        amount = amount - coin #next coin here
        current = table[amount]
    coins.sort()
    return coins

def _initializeTable(amount):
    table = [UNTOUCHED] * (amount + 1) 
    table[0] = BASE
    return table

def _getMinCoin(coinList, amount, table):
    """
    [INT] coinList, int amount, [(int,int)] table
    returns: (int minimum coins, int lastCoinUsed)
    """
    #BASE CASE
    if amount < 0:
        return IMPOSSIBLE_AMOUNT
    elif table[amount] != UNTOUCHED:
        return table[amount]
    
    #RECURSIVE CASE
    currentMinimum = UNTOUCHED
    currentCoin = NO_COIN
    for coin in coinList:
        newAmount = amount - coin
        previousMinimum = _getMinCoin(coinList, newAmount, table) #find min of previous amounts
        if previousMinimum != IMPOSSIBLE_AMOUNT:
            if currentMinimum == UNTOUCHED or previousMinimum < currentMinimum:
                currentMinimum = previousMinimum
                currentCoin = coin
    
    #SET DP TABLE
    if currentMinimum == UNTOUCHED:
        tableVal = IMPOSSIBLE_AMOUNT
    else:
        tableVal = (currentMinimum[0] + 1, currentCoin)
    table[amount] = tableVal
    
    return tableVal
        
class Tester(unittest.TestCase):

    def test_mincoin(self):
        self.assertEqual(minCoin([1,5,10,25],75), 3)
        
    def test_mincoin2(self):
        self.assertEqual(minCoin([1,3,7],100), 16)
    
    def test_mincoin3(self):
        self.assertEqual(minCoin([3,1,5,10,25],17), 4)
    
    def test_getChange(self):
        self.assertEqual(getChange([1,5,10,25],75), [25,25,25])
        
    def test_getChange2(self):
        self.assertEqual(getChange([1,3,7], 50), [1,7,7,7,7,7,7,7] )
    
    def test_getChangeEdge(self):
        self.assertEqual(getChange([],0), [])

if __name__ == '__main__':
    unittest.main()

                
                
                    
                    
                
                    
                
                    