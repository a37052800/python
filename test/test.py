a=[0,0,0,0,0,0,0]
sum=0
for i in range(1,7):
    print("請輸入第",i,"個學生資料")
    a[i]=int(input())
    sum+=a[i]
ar=sum/6
for i in range(1,7):
    if a[i]-ar>=5:
        print("A")
        continue
    if a[i]-ar>=2:
        print("B")
        continue
    if a[i]-ar>=0:
        print("C")
        continue
    else:
        print("D")
        continue