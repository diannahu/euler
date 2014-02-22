import math
import sys

def sieve(n):
  primes = [True] * (n+1)
  for i in xrange(2, int(math.sqrt(n)) + 1):
    if primes[i]:
      for j in xrange(i*i, n + 1, i):
        primes[j] = False

  return primes

num = 600851475143

starter = int(math.sqrt(num))
primes = sieve(starter)

for p in xrange(starter,-1,-1):
  if primes[p] and num % p == 0:
    print p
    sys.exit()