def true_func():
    print("Running true_func()")
    return True


def false_func():
    print("Running false_func()")
    return False


print(true_func() and false_func())  # Caso 1

print(false_func() and true_func())# Caso 2

print(true_func() and true_func())# Caso 3
