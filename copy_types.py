import copy

# Shallow Copy
print('--- Shallow Copy ---')
a = [[1, 2, 3], [4, 5, 6]]
a_copy = copy.copy(a)

print('Original List : ', a)
print('ID of the original list',  id(a))

a_copy[1][2] = 'x'

print('\nCopy List : ', a_copy)
print('Original List Now : ', a)
print('ID of the copied list : ', id(a_copy))


# Deep Copy
print('\n--- Deep Copy ---')
b = [[1, 2, 3], [4, 5, 6]]

print('Original List : ', b)
print('ID of the original list',  id(b))

b_deepcopy = copy.deepcopy(b)

b_deepcopy[1][2] = 'x'

print('\nCopy List : ', b_deepcopy)
print('Original List Now : ', b)
print('ID of the copied list : ', id(b_deepcopy))