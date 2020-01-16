def multi():
    su=0
    for i in range(1,1001):
        if((i%3==0)|(i%5==0)):
            su+=i
    print(su)   
multi()
