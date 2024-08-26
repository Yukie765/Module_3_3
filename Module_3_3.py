def print_params(a=1, b='str', c=True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print('--------')

value_list = [[1,2,3], False, 0.25]
value_dict = {'a':1, 'b':0.07, 'c':'kuku'}

print_params(*value_list)
print_params(**value_dict)
print('--------')

value_list2 = 1.23, 'hi'
print_params(*value_list2, 42 )


