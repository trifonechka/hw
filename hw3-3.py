def test(*args):
    print(args)


test('lion', 'rat', 'dog', 'monkey')



def factorial(n):
    if n == 1:
        return 1
    factorian_n_minus_1 = factorial(n=n-1)
    return n * factorian_n_minus_1


print(factorial(9))
