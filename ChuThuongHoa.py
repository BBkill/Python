

s=input()
ss=s
thuong=0
hoa=0
for c in s:
    if ord(c)>96:
        thuong=thuong+1
    else:
        hoa=hoa+1
if thuong>=hoa:
    print(ss.lower())
else:
    print(ss.upper())
