import math
import sys

def sieve(n):
    primes = [True] * (n+1)
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in xrange(i*i, n + 1, i):
                primes[j] = False

    return primes

num = 1999999

primes = sieve(num)
primes[0] = primes[1] = False

pinlist = [i for (i,v) in enumerate(primes) if v]
print sum(pinlist)
