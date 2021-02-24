import matplotlib.pyplot as plt
dx=[]
dy=[]
for i in range(0,10):
    dx.append(i)
    dy.append(i)
plt.plot(dx, dy, color='b')
plt.xlabel('t(s)') # 設定x軸標題
plt.xticks(dx, rotation='vertical') # 設定x軸label以及垂直顯示
plt.title('x(m)') # 設定圖表標題
plt.show()