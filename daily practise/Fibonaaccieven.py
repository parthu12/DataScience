def sumF():
    su=1
    b=2
    s=0
    for i in range(1,10):
        add=0
        add = su+b
        su=b
        b=add
        if(add%2==0):
           s+=add
    print(s+2)
        
        
        
sumF()
    
