num = int(input("請輸入0~15之間的任一數字:"))
if num >= 10:
    if num == 10:
        print("A")
    elif num == 11:
        print("B")
    elif num == 12:
        print("C")
    elif num == 13:
        print("D")
    elif num == 14:
        print("E")
    elif num == 15:
        print("F")
else:
    print(num)
