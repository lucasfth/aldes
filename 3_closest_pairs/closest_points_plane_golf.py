n=int(input())
t=sorted([list(map(float,input().split())) for _ in range(n)],key=lambda x:x[0])
q=lambda a,b:((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
o=lambda a,b:(q(a,b),(a,b))
def di(t):
    m=t[len(t)//2][0]
    if(len(t)==2):return(q(t[0],t[1]),t)
    elif(len(t)==3):
        d=o(t[0],t[1])
        if q(t[0],t[2])<d[0]:d=o(t[0],t[2])
        elif q(t[1],t[2])<d[0]:d=o(t[1],t[2])
        return d
    l,r=di(t[:len(t)//2]),di(t[len(t)//2:])
    d=l if l[0]<r[0] else r
    s=sorted([p for p in t if abs(p[0]-m)<d[0]],key=lambda y:y[1])
    return min((o(s[i],s[j]) for i in range(len(s)) for j in range(i+1,min(i+7,len(s))) if q(s[i],s[j])<d[0]),default=d,key=lambda x:x[0])
r=di(t);print(r[1][0][0],r[1][0][1]);print(r[1][1][0],r[1][1][1])