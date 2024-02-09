def test(a, b):
    return a * b

a, b = 7, 4

print(test(a, b))

test(a, b)


def test_2(a, b, c):
    return (a + b) ** c

a, b, c = 9, 3, 2
print(test_2(a, b, c))

test_2(a, b, c)
