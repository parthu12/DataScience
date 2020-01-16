northSouth=["Green","Yellow","red"]
eastWest=["Green","Yellow","red"]
northLight = northSouth[0]
if (northLight =='Green'):
    northLight ='Red'
elif northLight=='Red':
    northLight ='Green'
ewLight=eastWest[0]
if (ewLight =='Green'):
    ewLight ='Red'
elif ewLight=='Red':
    ewLight ='Green'
assert(not(ewLight == 'Green' and northLight =='Green'),'Both signals should not be green')
