def count(pharse):
    lower = 0
    upper = 0

    for l in pharse:
     if l.islower():
         lower = lower +1

     elif l.isupper():
          upper = upper +1

    return lower,upper


print(count('AAvvxsdBFSmkdas'))


