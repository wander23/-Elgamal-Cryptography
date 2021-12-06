import random
def fermat(n):
    s = 0
    while (n % 2 == 0):
        s += 1
        n /= 2
    return s, int(n)

def millerRabin(n):
    if n % 2 == 0:
        return False
    a = random.randint(2,n-1)
    s, d = fermat(n - 1)
    if (a ** d) % n == 1:
        return True

    for i in range(0, s + 1):
        if a ** ((2**i)*d) % n == n - 1:
            return True

    return False


if __name__ == "__main__":
    print(millerRabin(64776253))
