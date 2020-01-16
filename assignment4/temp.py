F=input("enter a temp in farheinheat")
F=int(F)
C=input("enter temp in cel")
C=int(C)
def far(t):
    c=0
    c= (t-32)*5/9
    
    print("temp in cel is"+str(c))
def cel(t):
    f=0
    f=((t*9)/5)+32
    print("temp in far is"+str(f))
far(F)
cel(C)
