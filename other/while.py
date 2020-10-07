i = 0
x = 0
while True:
    t = int(input())
    if(t == -1):
        break
    i = i+1
    x = x + t
print("成績加總:", x, " ", "平均成績:", x/i)
