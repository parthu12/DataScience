a =input(" enter your marks")
a = int(a)
grade=input("grade")
myGrade ={
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5}
    
grade = int(grade)
if a>40 and grade <5:
     print(' student passed')
else :
    print("student failed")
