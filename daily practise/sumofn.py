n=int(input("enter a num"))
def sum(n):
    i=1
    n+=1
    su=0
    while(i<n):
        su+=i
        i+=1
    print("sum is"+str(su))
        
    
def esu(n):
    i=1
    n+=1
    su=0
    while(i<n):
       if (i%2)== 0:
            su+=i
       i+=1
    print("sum eis"+str(su))


def osum(n):
    i=1
    n+=1
    su=0
    while(i<n):
        if (i%2) != 0:
            su+=i
        i+=1
    print("sum ois"+str(su))
sum(n)
esu(n)
osum(n)

    
