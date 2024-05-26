L1 = [[1,2,3,4], [1,2,3,4] ,[1,2,3,4]]
L2 = []

#Transpose of matrix means to change the elment by row and column #\
#L1 be as [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]#

for i in range(4):
    s = []
    for j in range(3):
        s.append(L1[j][i])

    L2.append(s)


print(L2)

