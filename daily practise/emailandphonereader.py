import re
def getData(filepath):
    f=open(filepath,'r')
    fileContents=f.readlines()
    result=''
    for line in fileContents:
        result+=line
    f.close()
    return result
phoneRegex=re.compile('''(
(\+?\d{1,3})? #countrycode
(-)?#optional
(\d{3}) #areacode
(-)?#optional for readbility
(\d{3})#area code
(-)? #optional
(\d{4})#phone code
)''',re.VERBOSE|re.I)
emailReagex=re.compile('''(([a-z]+[a-z,0-9,\.]+)@
([a-z])+
\.
([a-z]+))
''',re.VERBOSE|re.I)
result =set()
fileContents=getData('\\Users\\parth\\Desktop\\par\\read.txt')
phonenum=phoneRegex.findall(fileContents)
print(fileContents)
emailid=emailReagex.findall(fileContents)
print(emailid)

for data in phonenum:
    print(data)

for data in emailid:
    print(data)

