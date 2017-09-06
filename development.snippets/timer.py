# import modules
import sys
import os
import time

# constants
EXECSCRIPT = "TorrentToMedia.py"
EXECPATH = "D:\\Feed.Me.Bytes\\d.downloading\\config\\"


def print_timing(func):
"""
time a function using time.clock() : being called by @function decorator
"""
    def wrapper(*arg):
    """
    wrapper
    """
        t1 = time.clock()
        res = func(*arg)
        t2 = time.clock()
        print("%s took %0.3f ms" % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

# declare the @ decorator just before the function, invokes print_timing()
@print_timing
def getPrimeList(n):
    """ returns a list of prime numbers from 2 to < n using a sieve algorithm"""
    if n < 2:  return []
    if n == 2: return [2]
    # do only odd numbers starting at 3
    s = range(3, n+1, 2)
    # n**0.5 may be slightly faster than math.sqrt(n)
    mroot = n ** 0.5
    half = len(s)
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m*m-3)//2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i+1
        m = 2*i+3
    return [2]+[x for x in s if x]

if __name__ == "__main__":
    print "prime numbers from 2 to <10,000,000 using a sieve algorithm"
    primeList = getPrimeList(10000000)
    time.sleep(2.5)
    
"""
my output -->
prime numbers from 2 to <10,000,000 using a sieve algorithm
getPrimeList took 4750.000 ms

Note1: If you have Windows, it is better to use the time.clock() function (updates 1000 times per second) rather than time.time() (updates 18.2 times per second).
"""
