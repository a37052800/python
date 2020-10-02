def f(x):
    return (3*x)-7+(5/x)
h=pow(2,-30)
n = float(input("a="))
if n == 0:
    print("不存在")
else:
    print("x在a的導數為:")
    print((f(n+h)-f(n))/h)
