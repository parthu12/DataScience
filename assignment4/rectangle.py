l=input("length of rect")
b=input("breadth of rect")
l =int(l)
b=int(b)
def perimeter(intl,intb):
     perimeter = 0
     perimeter = 2*(intl+intb)
     print("perimeter is"+str(perimeter))

def area(intl,intb):
     area = 0
     area = intl*intb
     print("area is"+str(area))

perimeter(l,b)
area(l,b)
