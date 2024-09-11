n=int(input())
ps=sorted([list(map(float,input().split())) for _ in range(n)],key=lambda x:x[0])
q=lambda a,b:((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
o=lambda a,b:(q(a,b),(a,b))
def di(ps):
    m = ps[len(ps)//2][0]
    if (len(ps)==2):return (q(ps[0],ps[1]),ps)
    elif (len(ps)==3):
        d = o(ps[0],ps[1])
        if q(ps[0], ps[2])<d[0]:d=o(ps[0],ps[2])
        elif q(ps[1],ps[2])<d[0]:d=o(ps[1], ps[2])
        return d
    l,r=di(ps[:len(ps)//2]),di(ps[len(ps)//2:])
    d=l if l[0]<r[0] else r
    s=sorted([p for p in ps if abs(p[0]-m)<d[0]],key=lambda y:y[1])
    return min((o(s[i],s[j]) for i in range(len(s)) for j in range(i+1,min(i+7,len(s))) if q(s[i],s[j])<d[0]),default=d,key=lambda x:x[0])
r=di(ps)
print(r[1][0][0],r[1][0][1])
print(r[1][1][0],r[1][1][1])
