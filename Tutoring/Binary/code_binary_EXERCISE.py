# -*- coding: utf-8 -*-
"""

@author: Michael Lee
"""

''' Your task is to implement a Binary class, which represents a 2-byte signed
    integer
    Binary objects are created from a string, consisting of up-to 16 binary digits
    (0 or 1); if less than 16-digits are provided, then the most-significant digit
    (whiich is character 0) is used to pad the string to the left, e.g.
    Binary("010") == Binary("0000 0000 0000 0010")
    Binary("110") == Binary("1111 1111 1111 1110")
    Note: spaces are just for visual clarity
    
    I have provided the stub methods that you need to implement below, do not
    change their name or signature; these are "magic methods" that allow one
    to write:
    Binary('01') + Binary('1') // == Binary('0')    
    Binary('1') == Binary('01') // False
    abs(Binary('11')) // Binary('01')
    int(Binary('1')) // -1
    int(Binary('0101')) // 5
    
    You are free to represent the internal state of a Binary however you want
    (just because a string is used to construct a Binary, doesn't mean that you
    must store the str as part of it's state although you may )
'''    


import unittest

class Binary:
    
    def __init__(self, digits):
        '''
        have a 16 character representation
        '''
        lengthDigit = len(digits)
        
        if lengthDigit > 16:
            self.value = digits[lengthDigit-16:]
        else:
            self.value = (16-lengthDigit)*digits[0] + digits
    
    
    
    def __eq__(self, other):
        ''' return boolean '''
        return self.value == other.value
    
    def __add__(self, other):
        ''' 
        using two's complement arithmetic (CANNOT USE __int__() here)
        return a new Binary object representing self + other
        '''
        carry = 0
        newValue = ''
        for i in range(15,0,-1):
            total = carry + int(self.value[i]) + int(other.value[i])
            carry = total//2
            newValue= str(total % 2) + str(newValue)
        
        return Binary(newValue)
        
            
        
    
    def __neg__(self):
        ''' return Binary, i.e. - self''' 
        newValue = ''
        for i in range(15,0,-1):
            if self.value[i] == '0':
                newValue = '1'+ newValue
            else:
                newValue = '0' + newValue
        return Binary(newValue) + Binary('01')
    
    
    def __abs__(self):
        ''' return Binary, viz. abs(self) '''
        #just negate if first value is negative
        if(self.value[0] == '1'):
            return -self
        else:
            return self
        
    
    def __int__(self):
        ''' return int, viz. int(self) '''
        total_sum = 0
        for i in range(1,len(self.value)):
            total_sum *= 2
            total_sum += int(self.value[i])
            
        if self.value[0] == '1':
            total_sum -= 32768
        return total_sum

    def __repr__(self):
        ''' return str; you may choose how to represent this Binary, but
            should display the binary digits in a visually appealing way
        '''
        return "REPRESENTATION: " + self.value
            
    
class Tester(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_value_undersixteen(self):
        self.assertEqual(Binary('0').value, '0000000000000000')
        
    def test_value_oversixteen(self):
        self.assertEqual(Binary('11110000111100001111').value, '0000111100001111')
    
    
    def test_equal(self):
        a = Binary('0')
        b= Binary('00')
        self.assertEqual(a == b, True)
        
    def test_notequal(self):
        a = Binary('10')
        b= Binary('00')
        self.assertEqual(a == b, False)
        
    def test_add_simple(self):
        a = Binary('0')
        b = Binary('1')

        self.assertEqual(a + b == Binary('1111111111111111'), True)
    
    def test_add_overflow(self):
        a = Binary('1')
        b = Binary('01')

        self.assertEqual(a+b == Binary('0'), True)
        
    def test_negate_simple(self):
        a = Binary('0')
        self.assertEqual(-a, -Binary('0'))
    
    def test_abs_simple(self):
        a = Binary('1')
        self.assertEqual(abs(a), Binary('01'))
        
    def test_integer(self):
        a = Binary('1')
        self.assertEqual(int(a), -1)
    def test_integer_harder(self):
        a = Binary('0101')
        self.assertEqual(a.__int__(), 5 )
        
    def test_representation(self):
        a = Binary('0101')
        self.assertEqual(a.__repr__(), 'REPRESENTATION: 0000000000000101')




if __name__ == '__main__':
    unittest.main()
    MINIMUM = Binary('1' + '0' * 15)   