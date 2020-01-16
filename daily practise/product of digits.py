n=int(input("enter a num"))
def prod(n):
    res=1
    while(n!=0):
        a=n%10
        res*=a
        n//=10
    print(res)
prod(n)
