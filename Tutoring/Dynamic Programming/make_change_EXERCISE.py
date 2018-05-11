# -*- coding: utf-8 -*-
"""
Created on Thu May 10 07:07:37 2018

@author: thurston
"""

'''
Implement a function that takes two parameters:
a sequence (logical set) of coins/denomiinations
some amount of money (in cents)
and returns the minimum number of coins that can be used to make exact change
or -1 if no exact change can be made
e.g. assert makeChange([3, 1, 5, 10, 25], 17) == 4

once that is completed, write another slightly different function that returns the actual list
of coins (in descending order) that can be used to make exact change, e.g.
makeChange([3, 1, 5, 10, 25], 17) -> [10, 5, 1, 1]  or [10, 3, 3, 1] (the
solution need not be unique)
'''
    
INVALID_AMT = (-1,-1)
BASE = (0,0)

class MIN_COINS():

    """**SOLUTION EXPLANATION**
    GIVEN: COINLIST denominations; ASSUME they are UNIQUE and POSITIVE

    NAIVE: TRY EVERY POSSIBLE COMBO, IDK HOW TO DO THIS OR EVEN TRY EFFICIENTLY

    DP: MEMOIZATION ALGORITHM

    1. CONSTRUCT DP list of tuples (int, int): DP_MEMO[AMOUNT]: (min number that it takes to sum AMOUNT, previous pointer); 
    2. MIN_SUM[AMOUNT] = MIN [(DP_MEMO[AMOUNT-coin]) for coin in coinList]
    3. MEMOIZE ALONG THE WAY TO REDUCE WORK
    
    GET CHANGE
    4*. To get coins, backtrace from DP_MEMO[amount] using back pointers
        
    """
    
    def __init__(self):
        """Summary
        """
        #Represents DP_MEMO[AMOUNT] = (min coins to get AMOUNT, previous pointer)
        self.DP_MEMO = [BASE]
    
    def __EXTEND_MEMO(self, extension):
        """Summary: helper to extend memo
        
        Args:
            extension (INT): Description
        
        Returns:
            LIST: Description
        """
        self.DP_MEMO.extend([None]*extension)
        return self.DP_MEMO
            
    def __isValidCoin(self, value):
        """Summary
        
        Args:
            value (TUPLE): Description
        
        Returns:
            INT: Description
        """
        return value != INVALID_AMT
    
    def getMinCoin(self,coinList, amount):
        """Summary: wrapper for getMinCoinTuple that just returns the int minCoins
        
        Args:
            coinList (LIST): Description
            amount (INT): Description
        
        Returns:
            INT: Description
        """
        self.coinList = coinList
        return self.__getMinCoinTuple(amount)[0]
    
    def __getMinCoinTuple(self, amount):
        """Summary: generates DP_MEMO, returns desired tuple
        
        Args:
            amount (INT): Description
        
        Returns:
            TUPLE: Description
        """
        if amount > len(self.DP_MEMO):
            self.__EXTEND_MEMO(amount - len(self.DP_MEMO)+1)
        if amount < 0:
            return INVALID_AMT
        if self.DP_MEMO[amount] != None:
            return self.DP_MEMO[amount]
        else:
            previousMinCoin = INVALID_AMT
            prevAmount = -1
            
            #GET OPTIMAL PREVIOUSMINCOIN
            for coin in self.coinList:
                prev = self.__getMinCoinTuple(amount - coin)
                if not self.__isValidCoin(previousMinCoin) and self.__isValidCoin(prev) or self.__isValidCoin(prev) and prev < previousMinCoin:
                    previousMinCoin = prev
                    prevAmount = amount - coin
            
            #CONSTRUCT NEW TUPLE FOR DP LIST
            newMinCoin = (previousMinCoin[0] + 1, prevAmount) if self.__isValidCoin(previousMinCoin) else INVALID_AMT 
            self.DP_MEMO[amount] = newMinCoin
            return newMinCoin
    
    def getChange(self, amount):
        """Summary: Backtracing method to get coins
        
        Args:
            amount (INT): Description
        
        Returns:
            LIST: Description
        """
        current = self.DP_MEMO[amount]
        coins = []
        while (current > BASE):
            coins.append(amount-current[1])
            amount = current[1]
            current = self.DP_MEMO[current[1]]
        coins.sort()
        return coins
            
        
        
class Tester(unittest.TestCase):

    """Summary
    """
    def test_mincoin(self):
        """Summary
        """
        Tester = MIN_COINS()
        self.assertEqual(Tester.getMinCoin([1,5,10,25],75), 3)
        self.assertEqual(Tester.getChange(75), [25,25,25])
        
    def test_mincoin2(self):
        """Summary
        """
        Tester = MIN_COINS()
        self.assertEqual(Tester.getMinCoin([1,3,7],100), 16)
        self.assertEqual(Tester.getChange(100), [1, 1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])
    
    def test_mincoin3(self):
        """Summary
        """
        Tester = MIN_COINS()
        self.assertEqual(Tester.getMinCoin([3,1,5,10,25],17), 4)
    

if __name__ == '__main__':
    unittest.main()

                
                
                    
                    
                
                    
                
                    