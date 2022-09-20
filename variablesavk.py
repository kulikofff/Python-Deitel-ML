z = 'global z'

def print_variables():
    y = 'local y in print_variables'
    print(y)
    print(z)
    return 'Spasibo'

print(print_variables())
print(y)