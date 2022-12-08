num = int(input("請輸入一個小於16的正整數:"))
if num > 15:
    num = 15
print("※ 使用產生器產生一次性的資料")
for i in range(1, num+1):
    print(i)
list = [n*n for n in range(1, num+1)]
print("生成的整數平方串列內為",list)
input("Press the \"Enter\" key to exit...")