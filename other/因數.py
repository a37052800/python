'''def F(a):
    i = 2
    while a > 1:
        if a/i == 1:
            break
        elif a % i == 0:
            a = int(a/i)
        else:
            i = i+1
    return a'''


ans = []
n = int(input())
i = 2
while n > 1:
    if n % i == 0:
        n = int(n/i)
        ans.append(i)
        i=2
    else:
        i = i+1
print(ans)
