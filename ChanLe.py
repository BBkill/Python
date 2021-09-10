t=int(input())
while t>0:
    t-=1
    s=input()
    sum=0
    check=True
    for i in range(len(s)):
        sum+=int(s[i])
    
    if sum%10==0:
        for i in range(len(s)-1):
            if abs(int(s[i])-int(s[i+1]))!=2:
                check=False
                break
    else: check=False
    if check==False: print("NO")
    else: print("YES")