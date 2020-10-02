def f(x):
    return (3*x)-7+(5/x)
x = float(input("a="))
if x == 0:
    print("不存在")
else:
    h = 1
    for i in range(64):
        print((f(x+h)-f(x))/h)
        h = h/2
