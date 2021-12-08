def Bezout(x,y):
    # Input: x, y 
    # Output: gdc, a, b 
    # note: 
    #   x*a + y*b = gdc
    #   gdc = GDC(x, y)

    mn = min(x,y)
    mx = max(x,y)

    if mn == 0: 
        return mx,1,0

    a1, a2 = 1, 0
    b1, b2 = 0, 1
    
    while (mn > 0):
        quotient = mx // mn
        remainder = mx % mn

        a = a2 - quotient*a1
        b = b2 - quotient*b1

        mx = mn
        mn = remainder
        a2, a1 = a1, a
        b2, b1 = b1, b

    return mx, a2, b2

def MulMod(x, y, mod): 
    # Input: x, y, MOD
    # Output: x*y mod MOD

    yb = bin(y).replace("0b", "") # convert decimal to binary

    p = int(yb[len(yb) - 1]) * x

    for i in range(len(yb)- 2, -1, -1 ):
        x = (2 * x) % mod
        z = int(yb[i]) * x
        p = (p + z) % mod

    return p

def PowerMod(x, y, mod):
    # Input: x, y, MOD
    # Output: x^y mod MOD
    
    p = 1
    yb = bin(y).replace("0b", "") # convert decimal to binary       

    for i in range(len(yb)):
        p = p**2 % mod
        if int(yb[i]) == 1:
            p = (x * p) % mod

    return p

def is_prime(n):
    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    for i in range(3, int(n**(1/2)) + 1, 2):
        if n % i == 0:
            return False

    return True

    
def safe_prime(n): # find first n safe prime
    # q is safe prime if:
    # q = 2*p + 1 (p is a prime)

    s_prime = [5]

    # find first n prime
    count = 1
    while count < n:
        p = s_prime[count - 1] + 2
        while True:
            if is_prime(p) and is_prime((p - 1) / 2):
                s_prime.append(p)
                count += 1
                break
            p += 2

    return s_prime
            


def CRT():
    pass



