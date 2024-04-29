n = int(input("enter the number"))
rev = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev*10 + r

print("reverse of the number", rev)