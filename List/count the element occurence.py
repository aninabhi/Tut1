l1 = ["A", "D", "M", "F", "R", "K", "J", "N", "A", "D", "M", "F", "A", "M", "J", "O", "G", "Q", "K"]
l2 = []

for x in l1:
    if x not in l2:
        l2.append(x)
        count = l1.count(x)
        l2.append(count)

print(l2)
