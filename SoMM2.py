t=int(input())
while t>0:
    t=t-1
    n=input()
    check=True
    for i in range(len(n)):
        if n[i]=='7' or n[i]=='4': continue
        else:
            check=False
            print("NO")
            break
    if  check==True: print("YES")
