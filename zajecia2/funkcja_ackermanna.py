def a(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return a(m-1, 1)
    elif m > 0 and n > 0:
        return a(m - 1, a(m, n - 1))


print(a(1, 1))
print(a(0, 2))
print(a(2, 0))
print(a(3, 3))
