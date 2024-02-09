def print_params(a=1, b='book', c=True):
    print(a, b, c)
    return a, b, c


values_list = ['yes', 89, 'a int']
values_dict = {'a': '1', 'b': 'book', 'c': 'True'}
values_list2 = ['boll', 222]

params = print_params(*values_list)
params2 = print_params(**values_dict)
params3 = print_params(*values_list2, 42)
print_params()
