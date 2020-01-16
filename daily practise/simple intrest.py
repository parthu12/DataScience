p=float(input("input princple"))
t=float(input("time"))
r=float(input("rate of intresst"))
def simpleIntrest(p,t,r):
    si=0
    si=p*t*r/100
    print("simple intrest is"+str(si))
simpleIntrest(p,t,r)

def compoundIntrest(p,t,r):
    amount=0
    amount=p*((1+(r/100))**t)
    ci=amount-p
    print("compound intrest"+str(ci))
compoundIntrest(p,t,r)
