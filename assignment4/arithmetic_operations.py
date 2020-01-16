a= input("enter a num")
b=input('enter another num')
a=int(a)
b=int(b)

def add(inta,intb):
    total = 0
    total = inta+intb
    print('the sum is'+str(total))
    return total
def subtract(inta,intb):
    total = 0
    total = inta-intb
    print('the subtract is'+str(total))
    return total
def multiply(inta,intb):
    total = 0
    total = inta*intb
    print('the multiply is'+str(total))
    return total
def divide(inta,intb):
    total = 0
    total = inta//intb
    print('the divide is'+str(total))
    return total


add(a,b)
subtract(a,b)
multiply(a,b)
divide(a,b)
