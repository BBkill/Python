t=int(input())
while t>0:
    t=t-1
    s=input()
    check=True
    for i in range(len(s)-1):
        if s[i]>s[i+1]:
            print("NO")
            check=False
            break
    if check==True:
        print("YES")
        