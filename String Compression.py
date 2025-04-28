s=input("Enter string:")
res=" "
c=1
for i in range(len(s)):
    if i+1<len(s)and s[i]==s[i+1]:
        c=c+1
    else:
        res=res+s[i]
        res=res+str(c)
        c=1
print(res)        
