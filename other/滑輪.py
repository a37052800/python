t = []
w = []
f = []
for i in range(2):
    t.append(input("使用滑輪："))
    w.append(input("物體重量："))
    f.append(input("施力多少已達平衡："))
print("=================================================")
print("{:<10s}\t| {:<8s}\t| {:<8s}".format("Type","物重","施力"))
for i in range(2):
    print("{:<10s}\t| {:<10s}\t| {:<10s}".format(t[i],w[i],f[i]))
print("=================================================")
