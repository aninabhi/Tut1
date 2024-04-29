n = int(input("enter the number"))
rev = 0
m=n
##Here putting the value of n as in loop the value become different , so take ##
##the actual or starting value of n##
while n > 0:
    r = n % 10
    n = n // 10
    rev = rev*10 + r
if m == rev:
    print("Number is pallindrome")
else:
    print("Number is not pallindrome")

