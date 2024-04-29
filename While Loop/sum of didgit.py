n = int(input("enter the number"))
sum = 0

while n > 0:
    r = n % 10
    n = n // 10
    sum = sum + r

print("Digit of sum =", sum)
