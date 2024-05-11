s1 = input("Enter the first string ")
s2 = input("Enter the second string ")

a = sorted(s1)
b = sorted(s2)
print(a ,b)


if len(s1)==len(s2) and a == b:
    print("both words are Anagram")

else:
    print("not Anagram")

