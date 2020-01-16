s1=float(input ("enter mark1"))
s5=float(input ("enter mark5"))
s4=float(input ("enter mark4"))
s3=float(input ("enter mark3"))
s2=float(input ("enter mark2"))
def total(s1,s2,s3,s4,s5):
    total = 0
    total = s1+s2+s3+s4+s5
    print ("total marks"+str(total))
    return total
def average(tot):
    avg=0
    avg=tot/5
    print("avg"+str(avg))
    return avg
def percentage(total):
    per=0
    per=(total/500)*100
    print("percentage"+str(per))

tot=total(s1,s2,s3,s4,s5)
average(tot)
percentage(tot)
