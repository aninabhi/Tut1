def days():
    L = ("Sunday" , "Monday" , "Tuesday", "Wednesday", "Thrusday" , "Friday", "Satrurday")
    i =0

    while True:
        x = L[i]
        i = (i +1 ) % 7
        yield x


d =days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
