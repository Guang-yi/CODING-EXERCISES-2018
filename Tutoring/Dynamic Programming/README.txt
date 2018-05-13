**SOLUTION EXPLANATION**
GIVEN: COINLIST denominations; ASSUME they are UNIQUE and POSITIVE

NAIVE: TRY EVERY POSSIBLE COMBO, IDK HOW TO DO THIS OR EVEN TRY EFFICIENTLY

DP: MEMOIZATION ALGORITHM

1. CONSTRUCT table of tuples (int, int): table[AMOUNT]: (minCoinToMakeAmount, lastCoinAdded); 

MINCOIN EXAMPLE: minCoin(amount) OMITTED memo and coinlist for concision

EX. minCoin([1,2], 5, table)

    1. INIT TABLE:
        [BASE, UNTOUCHED, UNTOUCHED, UNTOUCHED, UNTOUCHED, UNTOUCHED]
        
    2. POPULATING TABLE RECURSIVE CALLS AND FINAL TABLE STATE:
        minCoin(5) with [1,2] coins:
        
        1.  minCoin(5) = min(minCoin(4), minCoin(3)) +1      
        2.  minCoin(4) = min(minCoin(3), minCoin(2)) +1        
        3.  minCoin(3) = min(minCoin(2), minCoin(1)) +1            
        4.  minCoin(2) = min(minCoin(1), minCoin(0)) +1        
        5.  minCoin(1) = min(minCoin(0)) +1
        
        FINAL STATE:
        [BASE, (1,1), (1,2), (2,2), (2,2), (3,1)]
        
        Return (3,1)
    
    3. MAKE CHANGE:
        
        makeChange(5):
        table[5] --> (3,1); add 1 
        table[5-1] --> table[4] --> (2,2); add 2
        table[4-2] --> table[2] --> (1,2); add 2
        table[2-2] --> table[0] --> (0,0); #base end
        
        returns [1,2,2]