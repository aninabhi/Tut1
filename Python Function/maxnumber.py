def max(a,b,c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(max(3,5,6))