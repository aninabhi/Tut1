n = int(input("enter the number"))
rev = 0
m=n

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev*10 + r
if m == rev:
    print("Number is pallindrome")
else:
    print("Number is not pallindrome")

