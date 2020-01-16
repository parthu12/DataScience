days=input("enter num of days")
days=int(days)
def conversion(d):
    years=0
    months=0
    day=0
    years=d//365
    weeks=(d%365)//7
    day=(d%365)%7
    print("no.of year is"+str(years))
    print("no.of weeks is"+str(weeks))
    print("no.of day is"+str(day))
conversion(days)
