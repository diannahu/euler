def findFactors(num):
    factors = {}
    maxNum = num
    i = 2

    while i <= maxNum:
        if maxNum % i == 0:
            try:
                factors[i] += 1
            except:
                factors[i] = 1
            maxNum = maxNum / i
        else:
            i += 1

    return factors

allFactors = {}
num = 1

for i in range(2,21):
    factors = findFactors(i)
    for key in factors.keys():
        if (not key in allFactors) or allFactors[key] < factors[key]:
            allFactors[key] = factors[key]

for factor,exponent in allFactors.items():
    num *= factor ** exponent

print num
