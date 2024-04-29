n = int(input("enter the number"))
bin = ' '

while n>0:
    r = n % 2
    n = n // 2
    bin = str(r) + bin

print(bin)


