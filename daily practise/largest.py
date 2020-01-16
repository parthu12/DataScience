a=float(input("enter a num"))
b=float(input("enter a num"))
c=float(input("enter a num"))
def largestof2(a,b):
    max=a if(a>b)else b
    print("max"+str(max))

largestof2(a,b)

def largestof3(a,b,c):
    max=a if(a>b)else b
    max1=c if c>max else max
    print("max of 3"+str(max1))

largestof3(a,b,c)
