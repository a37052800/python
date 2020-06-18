a = input()
for i in range(26):
    n = ord(a[i])-55
    if n >= 18:
        if n==18:
            n=34
        else:
            n-=1
            if n>=23:
                if n==23:
                    n=35
                else:
                    n-=1
                    if n>=30:
                        if n==30:
                            n=32
                        else:
                            n-=1
                            if n==32:
                                n=33
    print(n)
