#1a

def min_noreturn(a, b, c):
    minval = a
    if b < minval:
        minval = b
    if c < minval:
        minval = c
    print(minval)

#1b

def min_return(a, b, c):
    minval = a
    if b < minval:
        minval = b
    if c < minval:
        minval = c
    return minval


#2
def commonstring(a, b):
    common = ""
    for c in a:
        if c in b:
            common = common + c
    return common

#3
def alphabetical(a, b):
    if a < b:
        return True
    else:
        return False
    
def alphabetical_alternative(a, b):
    return a < b

#4
def biggestdivisor(n):
    for i in range(10, 0, -1):
        if n%i == 0:
            return i
    return 1
    

#5

def getinfo(a, b, c):
    minval = a
    if b < minval:
        minval = b
    if c < minval:
        minval = c

    maxval = a
    if b > maxval:
        maxval = b
    if c > maxval:
        maxval = c

    averg = (a+b+c)/3

    return (minval, maxval, averg)

# 6
def sharedvowels(s1, s2):
    vowels = "aeiou"
    shared = ""
    for c in vowels:
        if c in s1 and c in s2:
            shared = shared + c
    return shared, len(shared)

# 7
import random
def getdivis7():
    x = random.randint(0, 100)
    while x % 7 != 0:
        x = random.randint(0, 100)
    return x

    


# main
def main():

    #1a call
    min_noreturn(5, 10, 4)

    #1b call
    n1 = min_return(5, 10, 4)
    n2 = min_return(15, 3, 6)
    n3 = min_return(1, 7, 9)
    print(n1, n2, n3)

    # 1c call
    print(min_return(5,10,4),min_return(15,3,6),min_return(1,7,9))

    # 2 calls
    result = commonstring("elephant", "parasite")
    print(result)
    print(commonstring("dirigible", "binging"))

    # 3 call
    s1 = "turtle"
    s2 = "dog"
    s3 = "apple"
    if alphabetical(s1, s2):
        print(f"{s1} comes before {s2} in the alphabet")
    else:
        print(f"{s2} comes before {s1} in the alphabet")
        
    if alphabetical(s2, s3):
        print(f"{s2} comes before {s3} in the alphabet")
    else:
        print(f"{s3} comes before {s2} in the alphabet")

    # 4 call
    print(f"the largest divisor of 100 less than 10 is {biggestdivisor(100)}")
    print(f"the largest divisor of 49 less than 10 is {biggestdivisor(49)}")
    print(f"the largest divisor of 44 less than 10 is {biggestdivisor(44)}")
    print(f"the largest divisor of 17 less than 10 is {biggestdivisor(17)}")
    
    # 5 call
    print(getinfo(10, 34, 75))

    # 6 call
    w1 = "trampoline"
    w2 = "punctuated"
    vow, numvow = sharedvowels(w1, w2)
    print(f"{w1} and {w2} share {numvow} vowels: {vow}")

    # 7 call
    print(getdivis7())

main()
