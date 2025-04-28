def evaluate1(s):
    nums=[]
    symbol=[]
    precedence={"+"=1,"-"=1,"*"=2,"/"=2}
while(i<len(s)):
    if(s[i].isdigit):
        num=" "
        while(i<len(s) and s[i].isdigit):
             num=num+s[i]
             i=i+1
            nums.append(s[i])
     else:
         while(symbol and precedence[symbol[-1]]>=precedence[s[i]]):
             op=symbol.pop()
             n2=nums.pop()
             n1=nums.pop()
             if(op=="+"):
                 nums.append(n1+n2)
             elif(op=="-"):
                 nums.append(n1-n2)
             elif(op=="*"):
                 nums.append(n1*n2)
             elif(op=="/"):
                 nums.append(n1//n2)
        symbol.append(s[i])
        i=i+1
    while(symbol):
         pop=symbol.pop()
         n2=nums.pop()
         n1=nums.pop()
         elif(op=="+"):
            nums.append(n1+n2)
         elif(op=="-"):
            nums.append(n1-n2)
         elif(op=="*"):
            nums.append(n1*n2)
         elif(op=="/"):
            nums.append(n1//n2)
    res=nums.pop()
    return res
s="8/2+4/3*7
x=evaluate1(s)
print(x)
