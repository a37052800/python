def pr(c,n):
    for i in range(n):
        print(c, end="")
def prF(sum, num):
    pr(" ",sum-num)
    pr("*",2*num-sum)
def F(rang):
    for i in rang:
        prF(n, i)
        print()
n = eval(input())
F(range(n//2+1, n))
F(range(n, n//2-1, -1))
