yr=int(input("enter a year"))
def check(yr):
    leap= "true" if yr%4==0 else "false"
    if leap == "true":
        print("yr is leap"+str(yr))
    else  :
        print("yr is not leap"+str(yr))
check(yr)
