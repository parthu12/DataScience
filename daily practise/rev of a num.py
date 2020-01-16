n=int(input("enter a num"))
def rev(n):
    r=0
    while(n!=0):
        a=n%10
        print(a)
        r=(r*10)+a
        n//=10
    print(r)
rev(n)
