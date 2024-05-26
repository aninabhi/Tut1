l1 = [1,2,4,5,2,1,4,5,6,7,9,3,3,2,2,9,10,10,9]
l2 = []

for x in l1:
    if x not in l2:
        l2.append(x)
        count = l1.count(x)
        l2.append(count)

print(l2)