rad = input("enter radius")
rad=int(rad)
def dia(r):
    diameter = 0
    diameter= 2*r
    print("diameter"+str(diameter))
def circumference(r):
    circumference = 0
    circumference= (2*22*r)//7
    print("circumference"+str(circumference))
def area(r):
    area = 0
    area= (22*r**2)//7
    print("area"+str(area))
dia(rad)
circumference(rad)
area(rad)
