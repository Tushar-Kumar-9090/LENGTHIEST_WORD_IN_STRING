
## WAP to print lengthest word in a given string??

s="tus kum kumar tus pandaaaa tus kum"
s1=s.split()
d={}
for i in s1:
    if i not in d:
        d[i]=len(i)
mx=max(d.values())
for j in d:
    if d[j]==mx:
        print(j)

