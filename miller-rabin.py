import random
def fermat(n):
    s = 0
    while (n % 2 == 0):
        s += 1
        n /= 2
    return s, int(n)

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

def millerRabin(n):
    if n % 2 == 0:
        return False
    a = random.randint(2,n-1)
    s, d = fermat(n - 1)
    if  PowerMod(a,d,n) == 1:
        return True

    for i in range(0, s + 1):
        if PowerMod(a,(2**i)*d, n) == n - 1:
            return True

    return False


if __name__ == "__main__":
    print(millerRabin(6443456523532571586598761756129858921568791265789216578217856217856182956789216578235325235325634768347567843657894335789346789347897843784378947389634876789436789435784378436894374358996439941867489128493253534255326236327623673272347432743734743743743743743743753255893578932589793825235235578906753))
