list_nom = (382763, 991873, 993100, 2309109)


def test(*args):
    print(args)


test('lion', 'rat', 'dog', 'monkey')



def factorial(n):
    if n == 3:
        return 3
    factorian_n_minus_1 = factorial(n=n-1)
    return n * factorian_n_minus_1


print(factorial(9))
