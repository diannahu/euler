maxNum = 998001

def isPalindrome(number):
    strOfNum = str(number)
    i = 0
    j = len(strOfNum) - 1

    while (i < j):
        if strOfNum[i] != strOfNum[j]:
            return False
        i += 1
        j -= 1

    return True

def isDivisible(number):
    i = 999

    while i >= 100:
        if number % i == 0 and len(str(number / i)) == 3:
            return True
        i -= 1

    return False

while maxNum > 10000:
    if isPalindrome(maxNum) and isDivisible(maxNum):
        print maxNum
        break
    maxNum -= 1
