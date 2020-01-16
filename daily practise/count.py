n =int(input("enter a num"))
def count(n):
    coun=0
    while(n!=0):
        m=n//10
        n=m
        print(n)
        print(coun)
        coun+=1
        print(coun)
        
    print(coun)
count(n)
