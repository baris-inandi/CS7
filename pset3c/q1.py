def foo(x):
    return 1 - 2 * x


print(foo(3) + abs(foo(10)))
print(foo(foo(foo(foo(2)))))
