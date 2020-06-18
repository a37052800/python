ID = input()
lisWig = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
n = int(ord(ID[0]))-55
if n >= 18:
    if n == 18:
        n = 34
    else:
        n -= 1
        if n >= 23:
            if n == 23:
                n = 35
            else:
                n -= 1
                if n >= 30:
                    if n == 30:
                        n = 32
                    else:
                        n -= 1
                        if n == 32:
                            n = 33
# print(n)
listId = []
listId.append(int(n/10))
listId.append(int(n % 10))
for i in range(1, 10):
    listId.append(ord(ID[i])-48)
nans = 0
"""for i in range(11):
    print(listId[i], end=" ")"""
for i in range(11):
    nans += listId[i]*lisWig[i]
if(nans % 10 == 0):
    print("real")
else:
    print("fake")
