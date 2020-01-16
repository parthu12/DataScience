a= input("enter a num")
b=input('enter another num')
a=int(a)
b=int(b)

def sum(inta,intb):
    total = 0
    total = inta+intb
    print('the sum is'+str(total))
    return total

sum(a,b)
