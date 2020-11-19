def div(a):
    if a==1:
        return [1]
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
n=int(input())
i=3
x=0
while x<n :
    t=sum(div(i))
    if (sum(div(t))==i) and (t!=i) and (t>i):
        print("(",i,",",t,")")
        x=x+1
        i=i+1
    else:
        i=i+1