import sys

for a in xrange(1, 1001):
    for b in xrange(1, 1001):
        for c in xrange(1, 1001):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print a * b * c
                sys.exit(0)
