SZ=range(9);B=range(10);G=lambda p,q:not(p[0]//3-q[0]//3or p[1]//3-q[1]//3)or not(p[0]-q[0])*(p[1]-q[1])
C=lambda a:[((j,i),set(B[1:])if not a[i][j]else{a[i][j]})for j in SZ for i in SZ];k=lambda x:len(x[-1])
E=lambda a:any(any(c not in B for c in r)for r in a)or len(a)-len(SZ)or any(len(_)-len(SZ)for _ in a) 
def get_grid(c,r=[[0]*9for i in SZ]):
    for p,v in c:r[p[1]][p[0]]=v
    return r
def S(z,t):
    if t:#Clean Code Robert M. (* ^ ω ^)
        for _ in (a:=min(t,key=k)[0],b:=min(t,key=k)[1])[1]:yield from S([*z,[a,_]],[(p,d-{_}if G(a,p)else d)for p,d in t if p is not a ])
    else:yield z
def sudoku_solver(a):
    r=next(s:=S((),C(a)))
    if E(a)or next(s,0):raise # if no valid or more than 1 solution
    return get_grid(r)