def prime(n,a):
    if(n==1):
        return
    i=2
    while(n%i!=0):
        i=i+1
    print(i,end=" ")
    prime(n//i,a)
n=int(input("Enter any number:"))
prime(n,2)
