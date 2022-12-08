S = 0
B = 0
O = 0


def soP(so):
    for i in range(so):
        print(" *", end="")
    print()


def soB():
    print("==================================")
    print("S ", end="")
    soP(S)
    print("B ", end="")
    soP(B)
    print("O ", end="")
    soP(O)
    print("==================================")


ki = ""
while(ki != "x"):
    ki = input("請輸入(好球:1 壞球:0 結束:x): ")
    if(ki == "1"):
        S += 1
        if(S >= 3):
            O += 1
            S = 0
    elif(ki == "0"):
        B += 1
        if(B >= 4):
            S = 0
            B = 0
            O = 0
    soB()
