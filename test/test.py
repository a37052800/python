def div(a):
    ans=[]
    i=1
    while i<a/i:
        if a%i==0:
            ans.append(i)
            ans.append(int(a/i))
            i=i+1
        else:
            i=i+1
    ans.remove(a)
    return ans
print(div(6),sum(div(6)))