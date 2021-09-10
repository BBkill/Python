t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=input()
    A=a.split()
    for i in range(n):
        A[i]=int(A[i])
    A.sort()
    b=input()
    B=b.split()
    for i in range(n):
        B[i]=int(B[i])
    B.sort()
    check=True
    for i in range(n):
        if A[i]<=B[i]:
            continue
        else:
            check=False
            print("NO")
            break
    if check==True: print("YES")
