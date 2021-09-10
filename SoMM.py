n=input()
tmp=0
for i in range(len(n)):
    if n[i]=='7' or n[i]=='4': tmp=tmp+1
if tmp==4 or tmp == 7:
    print("YES")
else: print("NO")
