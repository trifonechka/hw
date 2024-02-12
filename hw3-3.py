list_nom = (382763, 991873, 993100, 2309109)


def test(nom=374278, word='добавь в', spisok=list_nom):
    print(nom, word, spisok)


test()


def factorial(n):
    if n == 3:
        return 3
    factorian_n_minus_1 = factorial(n=n-1)
    return n * factorian_n_minus_1


print(factorial(9))
