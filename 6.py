def getSum(num):
    if num == 0 or num == 1:
        return num
    return num + getSum(num - 1)

def getSumOfSquares(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i ** 2
    return sum

print getSum(100) ** 2 - getSumOfSquares(100)
