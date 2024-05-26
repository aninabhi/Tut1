food = ["pizza","burger","chowmin","pasta","cake","dosa","roll","momos"]

letter = input("enter the single letter  ")

for x in food:
    if x.startswith(letter):
        print(x)

else:
    print("no item available in list")



