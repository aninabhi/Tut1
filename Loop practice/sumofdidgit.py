enter_the_number = int(input("wishing any number"))
psum = 0
nsum = 0
count = 0

while count < enter_the_number:
    n = int(input("enter the number"))
    if n > 0:
        psum = psum + n
    else:
        nsum = nsum + n

    count += 1

print("sum of Posivite numbers=" , psum)
print("sum of Negative numbers=" , nsum)