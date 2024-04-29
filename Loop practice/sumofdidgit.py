enter_the_number = int(input("wishing any number"))
sum = 0
count = 0

while count < enter_the_number:
    n = int(input("enter the number"))
    sum = sum + n
    count = count + 1

print("sum of numbers=" , sum)