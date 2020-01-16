cm=input("enter a value to be converted")
cm = int(cm)
def meter(c):
    m = 0
    m=c/100
    print("in meter"+str(m))
def kilometer(c):
    km = 0
    km=c/(10**5)
    print("in meter"+str(km))
meter(cm)
kilometer(cm)
