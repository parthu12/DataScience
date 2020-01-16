n=int(input("enter a num"))
def fst(n):
    k=n
    while(n>10):
        f=n//10
        n=f
    l=k%10
    print("first"+str(n))
    print("last"+str(l))
    return n,l
j,l=fst(n)
def sum(n,l):
    add=0
    add=n+l
    print("sum"+str(add))
sum(j,l)
