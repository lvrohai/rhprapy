from math import sqrt

def is_prime(n):
    """ 判断素数 """
    assert n > 0
    for f in range(2, int(sqrt(n))+1):
        if n % f == 0:
            return False
    return True if n != 1 else False