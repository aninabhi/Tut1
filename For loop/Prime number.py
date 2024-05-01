n = int(input("enter the number"))
fact =0

for i in range(1, n+1):
    if n % i == 0:
        fact += 1

if fact == 2:
    print("Number is prime")


else:
    print("number is not prime as showing number of factors are ", fact)

