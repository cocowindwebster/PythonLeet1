#Solution 1 : TLE
"""
class Solution(object):
    def countPrimes(self, n):
        dict = {}
        count = 0
        for num in range(2, n):
            if dict.get(num, 0) == 0:
                count += 1
                number = num
                while number < n:
                    number += num
                    dict[number] = 1
        return count
"""

#Solution 2
class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False
        x = 2
        while x * x < n : # NOTE1: x * x is to filter the repetition
            if primes[x] :
                p = x * x
                while p < n:
                    primes[p] = False;
                    p += x
            x += 1
        return sum(primes)