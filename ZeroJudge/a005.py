for i in range(int(input())):
    a = input()
    l = list()
    for j in a.split(' '):
        l.append(int(j.strip()))
    # print(l)
    if(l[2]-l[1] == l[1]-l[0]):
        d = l[1]-l[0]
        for j in range(5):
            print(l[0]+d*j, end=' ')
    else:
        r = l[1]/l[0]
        for j in range(4):
            print(l[j],end=' ')
        print(int(l[3]*r))
    print('\n',end='')