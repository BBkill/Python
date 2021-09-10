t=int(input())
while t>0:
    t=t-1
    s=input()
    ss=""
    for i in range(len(s)-1):
        if  i%2==0:
            for j in range(int(s[i+1])):
                ss=ss+s[i]
    print(ss)