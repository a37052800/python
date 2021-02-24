p = []
print("N=",end="")
n = int(input())
print("key nember line by line")
for i in range(n):
    p.append(input())
a = 0
for i in range(n):
    for j in range(n):
        if j == i:
            continue
        for k in range(n):
            if k == j or k == i:
                continue
            for l in range(n):
                if l == k or l == j or l == i:
                    continue
                print(p[i], p[j], p[k], p[l])
                a = a+1
print(a)
