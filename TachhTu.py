s=input()
words=s.split()
n=len(words)-1
aw=[]
while n>=0:
    aw.append(words[n])
    n=n-1
print(" ".join(aw))
